"""
Author      : Akhilesh Mishra
Created At  : 21 July 2019
Description : Common interface for Batsman and Bowler class. Creates and regsiter the Batsman and Bowler object.
"""

from app.models.batsman import Batsman
from app.models.bowler import Bowler

class PlayerFactory:

    def __init__(self):
        self._creators = {}
# Register the object will be called through this inetrface
# Args format- type of object and Crator the actual class for which need to create an object
    def registerPalyerType(self, playerType, creator):
        self._creators[playerType] = creator

# Retunr the registered objects
# Args format type of object to be returned
    def getPlayerType(self,playerType):
        creator = self._creators.get(playerType)
        if not creator:
            raise ValueError(playerType)
        return creator()


playerFactory = PlayerFactory()
playerFactory.registerPalyerType('BATSMAN', Batsman)
playerFactory.registerPalyerType('WK-BATSMAN', Batsman)
playerFactory.registerPalyerType('ALLROUNDER', Batsman)
playerFactory.registerPalyerType('BOWLER', Bowler)


class PlayerInformation:
    #Create an object and call the appropriate class like bowler and Batsman
    # Args player info and playertype
    def serialize(self,player, playerType):
        playerTypeObject = playerFactory.getPlayerType(playerType)
        return playerTypeObject.addPlayer(player)
