"""
Author      : Deepak Terse
Created At  : 17 July 2019
Description : Class definition for model Bowler
"""

from app.models.player import Player
import json
class Bowler:
    id = ""
    playerId = ""
    matches = 0
    innings = 0
    runs = 0
    balls = 0
    wickets = 0
    bowlingAverage = 0
    bowlingAverage = 0
    name = ""
    role = ""
    battingStyle = ""
    bowlingStyle = ""
    country = ""
    battingInfo = {}
    bowlingInfo = {}
    isDeleted = False

    def addPlayer(self,bowler):

        self.id = bowler["id"]
        self.name = bowler["name"]
        self.role = bowler["role"]
        self.battingStyle = bowler["battingStyle"]
        self.bowlingStyle = bowler["bowlingStyle"]
        self.country = bowler["country"]
        self.playerId = bowler["playerId"]
        self.matches = bowler["matches"]
        self.innings = bowler["innings"]
        self.runs = bowler["runs"]
        self.balls = bowler["balls"]
        self.wickets = bowler["wickets"]
        self.bowlingAverage = bowler["runs"]/bowler["wickets"]
        self.bowlingStrikeRate = bowler["balls"]/bowler["wickets"]
        return self

