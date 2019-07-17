"""
Author      : Deepak Terse
Created At  : 15 July 2019
Description : All routes are specified here
"""

from flask import render_template
from flask import request, jsonify
import json
from app import app

#Sample Data

#app/static/player.json
playerInfoArray = [
    {
		"id" : "1",
        "name" : "Rohit Sharma",
        "role" : "Batsman",
        "battingStyle" : "Right Handed Bat",
        "bowlingStyle" : "Right-arm offbreak",
        "country" : "India"
	},
    {
		"id" : "2",
        "name" : "shikhar Dhawan",
        "role" : "Batsman",
        "battingStyle" : "Left Handed Bat",
        "bowlingStyle" : "Right-arm offbreak",
        "country" : "India"
	},
    {
		"id" : "3",
        "name" : "Mahendrasingh Dhoni",
        "role" : "WK-Batsman",
        "battingStyle" : "Right Handed Bat",
        "bowlingStyle" : "Right-arm medium",
        "country" : "India"
	},
    {
		"id" : "4",
        "name" : "Jasprit Bumrah",
        "role" : "Bowler",
        "battingStyle" : "Right Handed Bat",
        "bowlingStyle" : "Right-arm fast-medium",
        "country" : "India"
	},
    {
		"id" : "5",
        "name" : "Yuzvendra Chahal",
        "role" : "Bowler",
        "battingStyle" : "Right Handed Bat",
        "bowlingStyle" : "Right-arm legbreak",
        "country" : "India"
	}
]

#app/static/batsman.json
batsmenInfoArray = [
    {
        "id" : "1",
        "playerId" : "1",
        "matches" : 10,
        "innings" : 10,
        "runs" : 550,
        "balls" : 450
    },
    {
        "id" : "2",
        "playerId" : "2",
        "matches" : 10,
        "innings" : 10,
        "runs" : 350,
        "balls" : 410
    },
    {
        "id" : "3",
        "playerId" : "3",
        "matches" : 10,
        "innings" : 10,
        "runs" : 250,
        "balls" : 250
    }
]

#app/static/bowler.json
bowlerInfoArray = [
    {
        "id" : "1",
        "playerId" : "4",
        "matches" : 10,
        "innings" : 10,
        "runs" : 400,
        "balls" : 600,
        "wickets": 20
    },
    {
        "id" : "2",
        "playerId" : "5",
        "matches" : 10,
        "innings" : 10,
        "runs" : 500,
        "balls" : 600,
        "wickets": 10
    }
]

#app/static/team.json
teamInfoArray = [
    {
        "id" : "1",
        "name" : "India",
        "selected15" : ["1","2","3","4","5"]
    }
]

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

#app/models/batsman.py
class Batsmen:
    id = ""
    playerId = ""
    matches = 0
    innings = 0
    runs = 0
    balls = 0
    # highest = 0
    # Fours = 0
    # Sixes = 0
    # Fifties = 0
    # Hundreds = 0

    # def __init__(self):

#app/models/bowler.py
class Bowler:
    id = ""
    playerId = ""
    matches = 0
    innings = 0
    runs = 0
    balls = 0
    wickets = 0
    # maidens = 0

    # def __init__(self):

class Team:
    id = ""
    name = ""
    selected15 = []

    def __init__(self,team):
        self.id = team["id"]
        self.name = team["name"]
        self.selected15 = team["selected15"]


#Reusable Methods
#app/functions/query.py
def getAllPlayers():
    playersArray = []
    for player in playerInfoArray:
        playerObj = Player(player)
        playersArray.append(json.loads(json.dumps(playerObj.__dict__)))

    return playersArray

def getAllTeams():
    teamsArray = []
    for team in teamInfoArray:
        teamObj = Team(team)
        teamsArray.append(json.loads(json.dumps(teamObj.__dict__)))

    return teamsArray

# Views:
@app.route('/')
def index():
    return "Server Working"

@app.route('/viewPlayers', methods=['GET'])
def viewPlayers():
    responseData = {
        "response" : getAllPlayers()
    }
    
    return jsonify(responseData)

@app.route('/selectPlayer', methods=['GET'])
def selectPlayer():
    responseData = {
        "response" : getAllTeams()
    }
    
    return jsonify(responseData)