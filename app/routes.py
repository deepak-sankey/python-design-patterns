"""
Author      : Deepak Terse
Created At  : 15 July 2019
Description : All routes are specified here. This will be the entrypoint for all the requests
"""

from app.services.queries import getAllPlayers
from app import app
from flask import jsonify


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
