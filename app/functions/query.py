# import models.
from app.models.player import Player
# from app.routes import read_json_data

from flask import render_template
from flask import request, jsonify
import json
from app import app 
import os

def read_json_data(data_source):
   fp = open(data_source, encoding="utf8")
   data = json.loads(fp.read())
   return data

def getAllPlayers():
    playersArray = []
    playerInfoArray = read_json_data(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../database/player.json"))
    for player in playerInfoArray:
        playerObj = Player(player)
        playersArray.append(json.loads(json.dumps(playerObj.__dict__)))

    return playersArray