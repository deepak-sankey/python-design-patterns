from flask import render_template
from flask import request, jsonify
import json
from app import app 
import os

def read_json_data(data_source):
   fp = open(data_source, encoding="utf8")
   data = json.loads(fp.read())
   return data

#Class Definitions
#app/models/player.py
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
        # print(type(player)")
        self.id = player["id"]
        self.name = player["name"]
        self.role = player["role"]
        self.battingStyle = player["battingStyle"]
        self.bowlingStyle = player["bowlingStyle"]
        self.country = player["country"]
        
        batsmenInfoArray = read_json_data(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../database/batsman.json"))
        bowlerInfoArray = read_json_data(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../database/bowler.json"))

        
        if self.role == "Batsman" or self.role == "WK-Batsman" or self.role == "Batting Allrounder" or self.role == "Bowling Allrounder":
            battingInfo = list(filter(lambda item: self.id == item["playerId"], batsmenInfoArray))[0];
            self.battingInfo = {
                "id" : battingInfo["id"],
                "playerId" : battingInfo["playerId"],
                "matches" : battingInfo["matches"],
                "innings" : battingInfo["innings"],
                "runs" : battingInfo["runs"],
                "balls" : battingInfo["balls"]
            }
        else:
            bowlingInfo = list(filter(lambda item: self.id == item["playerId"], bowlerInfoArray))[0];
            self.bowlingInfo = {
                "id" : bowlingInfo["id"],
                "playerId" : bowlingInfo["playerId"],
                "matches" : bowlingInfo["matches"],
                "innings" : bowlingInfo["innings"],
                "runs" : bowlingInfo["runs"],
                "balls" : bowlingInfo["balls"],
                "wickets" : bowlingInfo["wickets"]
            }

        


