# routes.py

from flask import render_template
from flask import request, jsonify

from app import app

# Views:
@app.route('/')
def index():
    return "Server Working"

@app.route('/sampleApiCall', methods=['POST'])
def sampleApiCall():
    responseData = {}
    print(responseData)
    
    return jsonify(responseData), 200
