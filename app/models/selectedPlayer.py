"""
Author      : Vishal Panchal
Created At  : 18 July 2019
Description : Class definition for model selected player
"""

import json
from app import app
import os
from app.models.player import Player
from app.models.batsman import Batsman
from app.models.bowler import Bowler

class selectedPlayer(Player):
    playerId = ""
    name = ""
    role = ""
    team = ""

    def __init__(self, player):
        super().__init__(player)

        self.playerId = player["id"]
        self.name = player["name"]
        self.role = player["role"]
        self.team = player["country"]