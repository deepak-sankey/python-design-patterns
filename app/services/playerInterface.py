"""
Author      : Akhilesh Mishra
Created At  : 21 July 2019
Description : Common interface for Batsman and Bowler class. Creates and regsiter the Batsman and Bowler object.
"""

from app.models.batsman import Batsman
from app.models.bowler import Bowler

# Author : Akhilesh Mishra  
# This is class of PlayerFactory
class PlayerFactory:

    def __init__(self):
        self._creators = {}

    # Author : Akhilesh Mishra  
    # Register the object will be called through this inetrface
    # Args format- type of object and Crator the actual class for which need to create an object
    def registerPalyerType(self, playerType, creator):
        self._creators[playerType] = creator

    # Author : Akhilesh Mishra  
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


# Author : Akhilesh Mishra  
# To Create an object and call the appropriate class like bowler and Batsman
# Args player info and playertype
class PlayerInformation:
    def serialize(self,player, playerType):
        playerTypeObject = playerFactory.getPlayerType(playerType)

        return playerTypeObject.addPlayer(player)
