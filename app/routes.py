"""
Author      : Deepak Terse
Created At  : 15 July 2019
Description : All routes are specified here. This will be the entrypoint for all the requests
"""

from app.services.queries import getAllPlayers
from app.services.queries import getPlayer
from app.services.queries import getSelectedPlayerCount
from app.services.queries import isPlayerPresentInSelectedPlayer
from app.services.queries import addSelectedPlayer
from app.services.queries import getSelectedPlayers
from app.services.queries import removeSelectedPlayer

from app import app
from flask import jsonify
from flask import request


# Default route to check the server status
@app.route('/')
def index():
    return "Server Working"

# To view all the players
@app.route('/viewPlayers', methods=['GET'])
def viewPlayers():
    responseData = {
        "response" : getAllPlayers()
    }
    return jsonify(responseData)

#To add player in 15 member squad
@app.route('/addInSelectedPlayer', methods=['POST'])
def addInSelectedPlayer():
    incomingData = request.get_json()
    playerId = incomingData['Id']
    responseData = {
        "response" : addSelectedPlayer(playerId)
    }
    return responseData

#To remove player from 15 member squad
@app.route('/removeSelectedPlayerFromList', methods=['POST'])
def removeSelectedPlayerFromList():
    incomingData = request.get_json()
    playerId = incomingData['Id']
    reponseData = {
        "response" : removeSelectedPlayer(playerId)
    }
    return reponseData

#To view all the selected players
@app.route('/getSelectedPlayersList', methods=['GET'])
def getSelectedPlayersList():
    responseData = {
        "response" : getSelectedPlayers()
    }
    return responseData    