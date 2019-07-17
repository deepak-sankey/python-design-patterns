"""
Author      : Deepak Terse
Created At  : 15 July 2019
Description : All routes are specified here
"""

from flask import render_template
from flask import request, jsonify
import json
from app import app 
import os

from app.functions.query import getAllPlayers

#Sample Data
# data_source = os.path.join(os.path.dirname(os.path.realpath(__file__)), "database/player.json")

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


#Reusable Methods
#app/functions/query.py
# def getAllPlayers():
#     playersArray = []
#     playerInfoArray = read_json_data(os.path.join(os.path.dirname(os.path.realpath(__file__)), "database/player.json"))
#     for player in playerInfoArray:
#         playerObj = Player(player)
#         playersArray.append(json.loads(json.dumps(playerObj.__dict__)))

#     return playersArray


#Main Execution
# print("Main Execution started : ", getAllPlayers())


# Views:
@app.route('/')
def index():
    return "Server Working"

@app.route('/viewPlayers', methods=['GET'])
def viewPlayers():
    # print(getAllPlayers())
    print("@@@@@@@@@@@@@@@@@@@@@@@@")
    responseData = {
        "response" : getAllPlayers()
    }
    # AllPlayersInfo = json.dumps(responseData)
    # print(len(AllPlayersInfo))
    # print("==============",AllPlayersInfo[1])

    # print(AllPlayersInfo)
    
    return jsonify(responseData)