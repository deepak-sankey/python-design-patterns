"""
Author      : Deepak Terse
Created At  : 17 July 2019
Modified At : 21 July 2019 
Description : Class definition for model Player
"""

import json
from app import app
import os

# Author : Deepak Terse
# This is class of Bowler with __init__ function to add new player 
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

    # Author : Deepak Terse
    # Return nothing
    # Args player dictionary
    def __init__(self, player):
        self.id = player["id"]
        self.name = player["name"]
        self.role = player["role"]
        self.battingStyle = player["battingStyle"]
        self.bowlingStyle = player["bowlingStyle"]
        self.country = player["country"]
