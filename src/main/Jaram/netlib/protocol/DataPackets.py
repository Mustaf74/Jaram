# Jaram
# A MC:BE Software
# https://github.com/SFWTeam/Jaram
# By SFW-Team
# And GianC-Dev
#-------------------------------

from src.main.Jaram.netlib.protocol.DataPacket import DataPacket


class DATA_PACKET_0(DataPacket):
    @staticmethod
    def getPID(): return 0x80

class DATA_PACKET_1(DataPacket):
    @staticmethod
    def getPID(): return 0x81

class DATA_PACKET_2(DataPacket):
    @staticmethod
    def getPID(): return 0x82

class DATA_PACKET_3(DataPacket):
    @staticmethod
    def getPID(): return 0x83

class DATA_PACKET_4(DataPacket):
    @staticmethod
    def getPID(): return 0x84

class DATA_PACKET_5(DataPacket):
    @staticmethod
    def getPID(): return 0x85

class DATA_PACKET_6(DataPacket):
    @staticmethod
    def getPID(): return 0x86

class DATA_PACKET_7(DataPacket):
    @staticmethod
    def getPID(): return 0x87

class DATA_PACKET_8(DataPacket):
    @staticmethod
    def getPID(): return 0x88

class DATA_PACKET_9(DataPacket):
    @staticmethod
    def getPID(): return 0x89

class DATA_PACKET_A(DataPacket):
    @staticmethod
    def getPID(): return 0x8A

class DATA_PACKET_B(DataPacket):
    @staticmethod
    def getPID(): return 0x8B

class DATA_PACKET_C(DataPacket):
    @staticmethod
    def getPID(): return 0x8C

class DATA_PACKET_D(DataPacket):
    @staticmethod
    def getPID(): return 0x8D

class DATA_PACKET_E(DataPacket):
    @staticmethod
    def getPID(): return 0x8E

class DATA_PACKET_F(DataPacket):
    @staticmethod
    def getPID(): return 0x8F