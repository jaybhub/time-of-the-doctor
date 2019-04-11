"""
Enemy Class
    Enemy object created randomly from list in adventure game
    
    Parameters:
        power - amount of damage the enemy attack produces
        resourceName - the resource that must be depleted to kill enemy (e.g., health)
        resourceAmount - amount of resource that main character attacks must deplete to kill enemy
        
    Methods:
        getAttack - returns a damage amount to be inflicted on main character, equal to power
                    has a small chance to apply a damage multiplier with a value in a random range
                    prints notification of damage multiplier
"""

from random import randrange, random
from graphics import *

class Enemy:
    """Creates an enemy for a single battle with the main character"""
    def __init__( self, name, description, power, picture, resourceName, resourceAmount):
        self.name = name
        self.description = description
        self.power = int( power )
        self.picture = picture
        self.resourceName = resourceName
        self.resourceAmount = int( resourceAmount )
    
    def getName( self ):
        """Returns the name of the enemy"""
        return self.name
    
    def getDescription( self ):
        """Returns the description of the enemy"""
        return self.description
    
    def getPower( self ):
        """Returns the power of the enemy - the amount of damage
           the enemy will do before any multipliers are applied"""
        return self.power
    
    def getResourceName( self ):
        """Returns the resource the enemy needs to stay alive.
           Depleting this resource to 0 kills the enemy."""
        return self.resourceName
    
    def getResourceAmount( self ):
        """Returns the amount of the resource the enemy has to start battle"""
        return self.resourceAmount
    
    def getPicture( self ):
        """Returns the image file name of the enemy"""
        return self.picture
    
    def enemyAttacksHero( self ):
        """Returns a value to be applied as damage when the main character attacks
           Has a chance to trigger an attack multiplier to the damage. If so, prints
           a notification and amount of the multipler. Then returns multiplied value."""
        attack = self.power
        attackMultiplierChance = random()
        if attackMultiplierChance <= 0.1:
            attackMultiplier = randrange(2,4)
            print('Attack amplified {}x!'.format( attackMultiplier ) )
            attack = self.power * attackMultiplier
        return attack
    
    def takeDamage( self, damageInflicted):
        self.resourceAmount = self.resourceAmount - damageInflicted
  