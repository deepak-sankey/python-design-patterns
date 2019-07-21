"""
Author      : Digambar Gadekar
Created At  : 17 July 2019
Description : All queries made to the models or the database will be here
"""

#Models
from app.models.player import Player
from app.models.batsman import Batsman
from app.models.bowler import Bowler
from app.models.selectedPlayer import selectedPlayer

#Services
from app.services.utils import read_json_data
from app.services.utils import write_json_data
from app.services.playerInterface import PlayerInformation

#Libraries
import json
import os


#Path constants: Relative to this file
PATH_TO_PLAYER_JSON = "../database/player.json"
PATH_TO_BATSMAN_JSON = "../database/batsman.json"
PATH_TO_BOWLER_JSON = "../database/bowler.json"
PATH_TO_SELECTEDPLAYER_JSON = "../database/selectedPlayer.json"

#String constants
BATSMAN_ADDED = "Batsman added in the squad"
MAXIMUM_BATSMEN_REACHED = "Sorry! 7 Batsmen already present in the squad"
BOWLER_ADDED = "Bowler added in the squad"
MAXIMUM_BOWLERS_REACHED = "Sorry! 6 Bowlers already present in the squad"
WK_ADDED = "WK-Batsman added in the squad"
MAXIMUM_WK_ADDED = "Sorry! 2 WK-Batsmen already present in the squad"
PLAYER_PRESENT_IN_SQUAD = "Player already present in the squad"
SQUAD_COMPLETED = "15 Players already present in the squad"
PLAYER_REMOVED = "Player removed from the squad"
PLAYER_NOT_PRESENT_IN_SQUAD = "Player not present in the squad"


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

def getPlayer(playerId):
    playerFetched = {}
    playersArray = readPlayerJson()
    for player in playersArray:
        if (player["id"] == playerId):
            playerFetched = player
    return playerFetched

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
     #   return Batsman(player, battingInfo)
    #else:
     #   bowlingInfo = list(filter(lambda item: player["id"] == item["playerId"], bowlerInfoArray))[0]
      #  return Bowler(player, bowlingInfo)


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


#Model: SelectedPlayer
#Author: Vishal Panchal
#Created At: 20 July 2019

def isPlayerPresentInSelectedPlayer(playerId):
    playerPresent = False
    selectedPlayerArray = readSelectedPlayerJson()
    for player in selectedPlayerArray:
        if (player["id"] == playerId):
            playerPresent = True
    
    return playerPresent

def readSelectedPlayerJson():
    return read_json_data(os.path.join(os.path.dirname(os.path.realpath(__file__)), PATH_TO_SELECTEDPLAYER_JSON))

def getSelectedPlayers():
    selectedPlayersArray = readSelectedPlayerJson()

    return selectedPlayersArray

def addSelectedPlayer(playerId):
    response = ""
    fetchPlayer = getPlayer(playerId)
    addPlayer = {}
    if (getSelectedPlayerCount() < 15):
        if (isPlayerPresentInSelectedPlayer(playerId) == False):
            if (fetchPlayer["role"] == "Batsman"):
                if (getBatsmanCount() < 7):
                    selectedPlayerModel = selectedPlayer(fetchPlayer)
                    addPlayer = (json.loads(json.dumps(selectedPlayerModel.__dict__)))
                    response = BATSMAN_ADDED
                else:
                    response = MAXIMUM_BATSMEN_REACHED

            if (fetchPlayer["role"] == "Bowler"):
                if (getBowlerCount() < 6):
                    selectedPlayerModel = selectedPlayer(fetchPlayer)
                    addPlayer = (json.loads(json.dumps(selectedPlayerModel.__dict__)))
                    response = BOWLER_ADDED
                else:
                    response = MAXIMUM_BOWLERS_REACHED

            if (fetchPlayer["role"] == "WK-Batsman"):
                if (getWKCount() < 2):    
                    selectedPlayerModel = selectedPlayer(fetchPlayer)
                    addPlayer = (json.loads(json.dumps(selectedPlayerModel.__dict__)))
                    response = WK_ADDED
                else:
                    response = MAXIMUM_WK_ADDED
        else:
            response = PLAYER_PRESENT_IN_SQUAD
    else:
        response = SQUAD_COMPLETED

    path = PATH_TO_SELECTEDPLAYER_JSON
    if (bool(addPlayer)):
        readSelectedArray = readSelectedPlayerJson()
        readSelectedArray.append(json.loads(json.dumps(addPlayer)))
        write_json_data(path,readSelectedArray)

    return response

def removeSelectedPlayer(playerId):
    reponse = ""
    if(isPlayerPresentInSelectedPlayer(playerId)):
        selectedPlayersList = getSelectedPlayers()
        count = -1
        for player in selectedPlayersList:
            count+=1
            if (player["playerId"] == playerId):
                del selectedPlayersList[count]
                response = PLAYER_REMOVED
                break

        path = PATH_TO_SELECTEDPLAYER_JSON
        write_json_data(path,selectedPlayersList)
    else:
        response = PLAYER_NOT_PRESENT_IN_SQUAD

    return response

def getSelectedPlayerCount():
    count = 0
    selectedPlayerArray = readSelectedPlayerJson()

    return len(selectedPlayerArray)

def getBatsmanCount():
    count = 0
    batsmenArray = readSelectedPlayerJson()
    for batsmen in batsmenArray:
        if (batsmen["role"] == "Batsman"):
            count+=1

    return count

def getBowlerCount():
    count = 0
    bowlerArray = readSelectedPlayerJson()
    for bowler in bowlerArray:
        if (bowler["role"] == "Bowler"):
            count+=1
    
    return count

def getWKCount():
    count = 0
    wkArray = readSelectedPlayerJson()
    for wk in wkArray:
        if (wk["role"] == "WK-Batsman"):
            count+=1

    return count
