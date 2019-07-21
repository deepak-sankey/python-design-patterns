"""
Author      : Deepak Terse
Created At  : 17 July 2019
Description : Class definition for model Batsman
"""

from app.models.player import Player
import json

class Batsman:
    id = ""
    playerId = ""
    matches = 0
    innings = 0
    runs = 0
    balls = 0
    battingAverage = 0
    battingStrikeRate = 0
    name = ""
    role = ""
    battingStyle = ""
    bowlingStyle = ""
    country = ""
    battingInfo = {}
    bowlingInfo = {}
    isDeleted = False

    def addPlayer(self,batsman):
        print(batsman)
        self.id = batsman["id"]
        self.name = batsman["name"]
        self.role = batsman["role"]
        self.battingStyle = batsman["battingStyle"]
        self.bowlingStyle = batsman["bowlingStyle"]
        self.country = batsman["country"]
        self.playerId = batsman["playerId"]
        self.matches = batsman["matches"]
        self.innings = batsman["innings"]
        self.runs = batsman["runs"]
        self.balls = batsman["balls"]
        self.battingAverage = batsman["runs"]/batsman["innings"]
        self.battingStrikeRate = batsman["runs"]*100/batsman["balls"]       
        return self