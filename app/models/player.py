"""
Author      : Deepak Terse
Created At  : 17 July 2019
Description : Class definition for model Player
"""

import json
from app import app
import os

class Player:
    id = ""
    name = ""
    role = ""
    battingStyle = ""
    bowlingStyle = ""
    country = ""
    battingInfo = {}
    bowlingInfo = {}
    isDeleted = False

    def __init__(self, player):
        self.id = player["id"]
        self.name = player["name"]
        self.role = player["role"]
        self.battingStyle = player["battingStyle"]
        self.bowlingStyle = player["bowlingStyle"]
        self.country = player["country"]
