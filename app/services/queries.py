"""
Author      : Digambar Gadekar
Created At  : 17 July 2019
Modified At : 21 July 2019 
Description : All queries made to the models or the database will be here
Dependancies: Data file "1.player.json , 2.batsman.json, 3.bowler.json" which contain player details.
"""

#Models
from app.models.player import Player
from app.models.batsman import Batsman
from app.models.bowler import Bowler

#Services
from app.services.utils import read_json_data
from app.services.playerInterface import PlayerInformation

#Libraries
import json
import os


#Path constants: Relative to this file
PATH_TO_PLAYER_JSON = "../database/player.json"
PATH_TO_BATSMAN_JSON = "../database/batsman.json"
PATH_TO_BOWLER_JSON = "../database/bowler.json"


# Author : Deepak Terse  
# This function is for read JSON file.
# Arg - Nothing
# Returns : Player JSON 
def readPlayerJson():
    return read_json_data(os.path.join(os.path.dirname(os.path.realpath(__file__)), PATH_TO_PLAYER_JSON))

# Author : Deepak Terse  
# This function is for read JSON data of player and return it as array format.
# Arg - Nothing
# Returns : Player Array
def getAllPlayers():
    try:
        playersArray = []
        playerInfoArray = readPlayerJson()
        for player in playerInfoArray:
            playerObj = createPlayer(player)
            playersArray.append(json.loads(json.dumps(playerObj.__dict__)))

        return playersArray
    except:
        result = {
           "status": "404",
           "data": "No player data found!"
       }
        return jsonify(result)

# Author : Digambar Gadekar  
# This function is for read JSON data of player and return it as array format.
# Arg - Nothing
# Returns : Player Array
def createPlayer(player):
    batsmenInfoArray = read_json_data(os.path.join(os.path.dirname(os.path.realpath(__file__)), PATH_TO_BATSMAN_JSON))
    bowlerInfoArray = read_json_data(os.path.join(os.path.dirname(os.path.realpath(__file__)), PATH_TO_BOWLER_JSON))

    #It returns the respective object depending on the role of the Player
    if player["role"] == "Batsman" or player["role"] == "WK-Batsman" or player["role"] == "Allrounder":
        playerInfo = list(filter(lambda item: player["id"] == item["playerId"], batsmenInfoArray))[0]
    else :
        playerInfo = list(filter(lambda item: player["id"] == item["playerId"], bowlerInfoArray))[0]

    player.update(playerInfo)
    playerInterace = PlayerInformation()
    return playerInterace.serialize(player,player["role"].upper())


# Author : Digambar Gadekar  
# This function is for read batsman JSON file.
# Arg - Nothing
# Returns : Batsman JSON 
def readBatsmanJson():
    return read_json_data(os.path.join(os.path.dirname(os.path.realpath(__file__)), PATH_TO_BATSMAN_JSON))

# Author : Digambar Gadekar  
# This function is for read JSON data of Batsmen and return it as array format.
# Arg - Nothing
# Returns : Batsmen Array
def getAllBatsmen():
    try:
        batsmenArray = []
        batsmanInfoArray = readBatsmanJson()
        for batsman in batsmanInfoArray:
            batsmanObj = Batsman(batsman)
            batsmenArray.append(json.loads(json.dumps(batsmanObj.__dict__)))

        return batsmenArray
    except:
        result = {
           "status": "404",
           "data": "No player data found!"
       }
        return jsonify(result)

# Author : Digambar Gadekar  
# This function is for read Bowler JSON file.
# Arg - Nothing
# Returns : Bowler JSON 
def readBowlerJson():
    return read_json_data(os.path.join(os.path.dirname(os.path.realpath(__file__)), PATH_TO_BOWLER_JSON))

# Author : Digambar Gadekar  
# This function is for read JSON data of Bowlers and return it as array format.
# Arg - Nothing
# Returns : Bowlers Array
def getAllBowlers():
    try:
        bowlersArray = []
        bowlerInfoArray = readBowlerJson()
        for bowler in bowlerInfoArray:
            bowlerObj = Bowler(bowler)
            bowlersArray.append(json.loads(json.dumps(bowlerObj.__dict__)))

        return bowlersArray
    except:
        result = {
           "status": "404",
           "data": "No player data found!"
       }
        return jsonify(result)