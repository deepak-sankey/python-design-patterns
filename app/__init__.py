"""
Author      : Deepak Terse
Created At  : 15 July 2019
Description : A flask application is initialised here
"""

from flask import Flask

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the routes
from app import routes

# Load the config file
app.config.from_object('config')

if __name__ == '__app__':
    app.run()