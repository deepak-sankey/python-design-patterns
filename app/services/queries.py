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

# Author : Vishal Panchal
# This function is to check if a player is already present in selected player JSON
# Arg - Player Id
# Returns : Boolean value
def isPlayerPresentInSelectedPlayer(playerId):
    playerPresent = False
    selectedPlayerArray = readSelectedPlayerJson()
    for player in selectedPlayerArray:
        if (player["id"] == playerId):
            playerPresent = True
    
    return playerPresent

# Author : Vishal Panchal
# This function is for read JSON data of selectedPlayer and return it as array format.
# Arg - Nothing
# Returns : SelectedPlayer JSON
def readSelectedPlayerJson():
    return read_json_data(os.path.join(os.path.dirname(os.path.realpath(__file__)), PATH_TO_SELECTEDPLAYER_JSON))

# Author : Vishal Panchal
# This function is for read JSON data of selectedPlayer and return it as array format.
# Arg - Nothing
# Returns : SelectedPlayer JSON
def getSelectedPlayers():
    selectedPlayersArray = readSelectedPlayerJson()

    return selectedPlayersArray

# Author : Vishal Panchal
# This function adds a player in selectedPlayer JSON file
# Arg - Player Id
# Returns : String based on the condition
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

# Author : Vishal Panchal
# This function removes a player from selectedPlayer JSON file
# Arg - Player Id
# Returns : String based on the condition
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

# Author : Vishal Panchal
# This function returns number of players present in selectedPlayer JSON file
# Arg - Nothing
# Returns : length of array
def getSelectedPlayerCount():
    selectedPlayerArray = readSelectedPlayerJson()

    return len(selectedPlayerArray)

# Author : Vishal Panchal
# This function returns number of batsmen present in selectedPlayer JSON file
# Arg - Nothing
# Returns : count
def getBatsmanCount():
    count = 0
    batsmenArray = readSelectedPlayerJson()
    for batsmen in batsmenArray:
        if (batsmen["role"] == "Batsman"):
            count+=1

    return count

# Author : Vishal Panchal
# This function returns number of bowlers present in selectedPlayer JSON file
# Arg - Nothing
# Returns : count
def getBowlerCount():
    count = 0
    bowlerArray = readSelectedPlayerJson()
    for bowler in bowlerArray:
        if (bowler["role"] == "Bowler"):
            count+=1
    
    return count

# Author : Vishal Panchal
# This function returne number of WK-batsmen present in selectedPlayer JSON file
# Arg - Nothing
# Returns : count
def getWKCount():
    count = 0
    wkArray = readSelectedPlayerJson()
    for wk in wkArray:
        if (wk["role"] == "WK-Batsman"):
            count+=1

    return count
