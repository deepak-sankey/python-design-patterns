"""
Author      : Digambar Gadekar
Created At  : 17 July 2019
Description : All queries made to the models or the database will be here
"""

#Models
from app.models.player import Player
from app.models.batsman import Batsman
from app.models.bowler import Bowler

#Services
from app.services.utils import read_json_data

#Libraries
import json
import os


#Path constants: Relative to this file
PATH_TO_PLAYER_JSON = "../database/player.json"
PATH_TO_BATSMAN_JSON = "../database/batsman.json"
PATH_TO_BOWLER_JSON = "../database/bowler.json"


#Model: Player
def readPlayerJson():
    return read_json_data(os.path.join(os.path.dirname(os.path.realpath(__file__)), PATH_TO_PLAYER_JSON))

def getAllPlayers():
    playersArray = []
    playerInfoArray = readPlayerJson()
    for player in playerInfoArray:
        playerObj = createPlayer(player)
        playersArray.append(json.loads(json.dumps(playerObj.__dict__)))

    return playersArray

def createPlayer(player):
    batsmenInfoArray = read_json_data(os.path.join(os.path.dirname(os.path.realpath(__file__)), PATH_TO_BATSMAN_JSON))
    bowlerInfoArray = read_json_data(os.path.join(os.path.dirname(os.path.realpath(__file__)), PATH_TO_BOWLER_JSON))

    #It returns the respective object depending on the role of the Player
    if player["role"] == "Batsman" or player["role"] == "WK-Batsman" or player["role"] == "Allrounder":
        battingInfo = list(filter(lambda item: player["id"] == item["playerId"], batsmenInfoArray))[0];
        return Batsman(player, battingInfo)
    else:
        bowlingInfo = list(filter(lambda item: player["id"] == item["playerId"], bowlerInfoArray))[0];
        return Bowler(player, bowlingInfo)


#Model: Batsman
def readBatsmanJson():
    return read_json_data(os.path.join(os.path.dirname(os.path.realpath(__file__)), PATH_TO_BATSMAN_JSON))

def getAllBatsmen():
    batsmenArray = []
    batsmanInfoArray = readBatsmanJson()
    for batsman in batsmanInfoArray:
        batsmanObj = Batsman(batsman)
        batsmenArray.append(json.loads(json.dumps(batsmanObj.__dict__)))

    return batsmenArray

#Model: Bowler
def readBowlerJson():
    return read_json_data(os.path.join(os.path.dirname(os.path.realpath(__file__)), PATH_TO_BOWLER_JSON))

def getAllBowlers():
    bowlersArray = []
    bowlerInfoArray = readBowlerJson()
    for bowler in bowlerInfoArray:
        bowlerObj = Bowler(bowler)
        bowlersArray.append(json.loads(json.dumps(bowlerObj.__dict__)))

    return bowlersArray
