"""
Author      : Deepak Terse
Created At  : 17 July 2019
Description : Class definition for model Batsman
"""

from app.models.player import Player

class Batsman(Player):
    id = ""
    playerId = ""
    matches = 0
    innings = 0
    runs = 0
    balls = 0
    battingAverage = 0
    battingStrikeRate = 0

    def __init__(self, player, batsman):
        super().__init__(player)

        self.id = batsman["id"]
        self.playerId = batsman["playerId"]
        self.matches = batsman["matches"]
        self.innings = batsman["innings"]
        self.runs = batsman["runs"]
        self.balls = batsman["balls"]
        self.battingAverage = batsman["runs"]/batsman["innings"]
        self.battingStrikeRate = batsman["runs"]*100/batsman["balls"]
