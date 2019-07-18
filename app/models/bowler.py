"""
Author      : Deepak Terse
Created At  : 17 July 2019
Description : Class definition for model Bowler
"""

from app.models.player import Player

class Bowler(Player):
    id = ""
    playerId = ""
    matches = 0
    innings = 0
    runs = 0
    balls = 0
    wickets = 0
    bowlingAverage = 0
    bowlingAverage = 0

    def __init__(self, player, bowler):
        super().__init__(player)

        self.id = bowler["id"]
        self.playerId = bowler["playerId"]
        self.matches = bowler["matches"]
        self.innings = bowler["innings"]
        self.runs = bowler["runs"]
        self.balls = bowler["balls"]
        self.wickets = bowler["wickets"]
        self.bowlingAverage = bowler["runs"]/bowler["wickets"]
        self.bowlingStrikeRate = bowler["balls"]/bowler["wickets"]
