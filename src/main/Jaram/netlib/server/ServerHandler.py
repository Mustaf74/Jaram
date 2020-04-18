# Jaram
# A MC:BE Software
# https://github.com/SFWTeam/Jaram
# By SFW-Team
# And GianC-Dev
#-------------------------------
from src.main.Jaram.netlib.Binary import Binary
from src.main.Jaram.netlib.NetLib import NetLib
from src.main.Jaram.netlib.protocol import EncapsulatedPacket
import time
from src.main.Jaram.netlib.server import NetLibServer, ServerInstance


class ServerHandler:
    server = None
    instance = None

    def __init__(self, server: NetLibServer, instance: ServerInstance):
        self.server = server
        self.instance = instance

    def sendEncapsulated(self, identifier: str, packet: bytearray, flags: int = NetLib.PRIORITY_NORMAL):
        buffer = ""
        buffer += chr(NetLib.PACKET_ENCAPSULATED)
        buffer += chr(len(identifier))
        buffer += identifier
        buffer += chr(flags)
        buffer += packet.toBinary(True)

        self.server.pushMainToThreadPacket(buffer)

    def sendRaw(self, address: str, port: int, payload: bytearray):
        buffer = chr(NetLib.PACKET_RAW) + chr(len(address)) + address + str(Binary.writeShort(port)) + payload
        self.server.pushMainToThreadPacket(buffer)

    def closeSession(self, identifier: str, reason: str):
        buffer = chr(NetLib.PACKET_CLOSE_SESSION) + chr(len(identifier)) + identifier + chr(len(reason)) + reason
        self.server.pushMainToThreadPacket(buffer)

    def sendOption(self, name: str, value: str):
        buffer = chr(NetLib.PACKET_SET_OPTION) + chr(len(name)) + name + value
        self.server.pushMainToThreadPacket(buffer)

    def blockAddress(self, address: str, timeout: int):
        buffer = chr(NetLib.PACKET_BLOCK_ADDRESS) + chr(len(address)) + address + str(Binary.writeInt(timeout))
        self.server.pushMainToThreadPacket(buffer)

    def shutdown(self):
        self.server.shutdown()
        buffer = chr(NetLib.PACKET_SHUTDOWN)
        self.server.pushMainToThreadPacket(buffer)
        time.sleep(50000 / 1000000.0) # Sleep for 1 tick

    def emergencyShutdown(self):
        self.server.shutdown()
        self.server.pushMainToThreadPacket("\x7f") # Emergency Shutdown

    def invalidSession(self, identifier):
        buffer = chr(NetLib.PACKET_INVALID_SESSION) + chr(len(identifier)) + identifier
        self.server.pushMainToThreadPacket(buffer)

    def handlePacket(self):
        packet = self.server.readThreadToMainPacket()
        if packet == None:
            return
        if len(packet) > 0:
            id = ord(packet[0])
            offset = 1
            if id == NetLib.PACKET_ENCAPSULATED:
                offset += 1
                length = ord(packet[offset])
                identifier = packet[offset:offset+length]
                offset += length + 1
                flags = ord(packet[offset])
                buffer = packet[offset:]
                self.instance.handleEncapsulated(identifier, EncapsulatedPacket.fromBinary(buffer, True), flags)
            elif id == NetLib.PACKET_RAW:
                length = ord(packet[offset])
                offset += 1
                address = packet[offset:offset+length]
                offset += length
                port = Binary.readShort(packet[offset:offset+2])
                offset += 2
                payload = packet[offset:]
                self.instance.handleRaw(address, port, payload)
            elif id == NetLib.PACKET_SET_OPTION:
                length = ord(packet[offset])
                offset += 1
                name = packet[offset:offset+length]
                offset += length
                value = packet[offset:]
                self.instance.handleOption(name, value)
            elif id == NetLib.PACKET_OPEN_SESSION:
                offset += 1
                length = ord(packet[offset])
                identifier = packet[offset:offset+length]
                offset += length + 1
                length = ord(packet[offset])
                address = packet[offset:offset+length]
                offset += len
                port = Binary.readShort(packet[offset:offset+2])
                offset += 2
                clientID = Binary.readLong(packet[offset:offset+8])
                self.instance.openSession(identifier, address, port, clientID)
            elif id == NetLib.PACKET_CLOSE_SESSION:
                length = ord(packet[offset])
                offset += 1
                identifier = packet[offset:offset+length]
                offset += length
                length = ord(packet[offset])
                offset += 1
                reason = packet[offset:offset+length]
                self.instance.closeSession(identifier, reason)
            elif id == NetLib.PACKET_INVALID_SESSION:
                offset += 1
                length = ord(packet[offset])
                identifier = packet[offset:offset+length]
                self.instance.closeSession(identifier, "Invalid session")
            elif id == NetLib.PACKET_ACK_NOTIFICATION:
                offset += 1
                length = ord(packet[offset])
                identifier = packet[offset:offset+length]
                offset += length
                identifierACK = Binary.readInt(packet[offset:offset+4])
                self.instance.notifyACK(identifier, identifierACK)
            return True
        return False
