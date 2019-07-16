"""
Author      : Deepak Terse
Created At  : 15 July 2019
Description : All routes are specified here
"""

from flask import render_template
from flask import request, jsonify

from app import app

# Views:
@app.route('/')
def index():
    return "Server Working"

@app.route('/addPlayer', methods=['POST'])
def addPlayer():
    responseData = {}
    print(responseData)
    
    return jsonify(responseData), 200

@app.route('/updatePlayer', methods=['POST'])
def updatePlayer():
    responseData = {}
    print(responseData)
    
    return jsonify(responseData), 200

@app.route('/deletePlayer', methods=['POST'])
def deletePlayer():
    responseData = {}
    print(responseData)
    
    return jsonify(responseData), 200

@app.route('/viewPlayers', methods=['POST'])
def viewPlayers():
    responseData = {}
    print(responseData)
    
    return jsonify(responseData), 200

@app.route('/sampleApiCall', methods=['POST'])
def sampleApiCall():
    responseData = {}
    print(responseData)
    
    return jsonify(responseData), 200
