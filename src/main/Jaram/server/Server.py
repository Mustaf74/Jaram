"""
       _              _____               __  __
      | |     /\     |  __ \      /\     |  \/  |
      | |    /  \    | |__) |    /  \    | \  / |
  _   | |   / /\ \   |  _  /    / /\ \   | |\/| |
 | |__| |  / ____ \  | | \ \   / ____ \  | |  | |
  \____/  /_/    \_\ |_|  \_\ /_/    \_\ |_|  |_|

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU Lesser General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  @author SFWTeam
  @link https://github.com/SFWTeam

"""

import src.main.Jaram.player.Player as Player

activedplugins = ['']
pname = ['']
papi = ['']
pver = ['']
pcmd = ['']
pcmdinfo = ['']
players = ['']
playersip = ['']
status = ['']


def server(self):
    pass


def start(self):
    status.clear()
    status.append('activated')


def stop(self):
    status = 'deactived'


def getPlayer(self):
    return Player
