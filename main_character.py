"""
MainCharacter Class
    Parameters:
        name - allows for user input with small modification
        regenerations - resets character health to 100%
        
    Methods:
        attack - takes a random value from randrange
                 has a small chance for an attack multiplier
                 attack multiplier amount is also random
                 prints notification of damage multiplier
            *used by Enemy class during battle
            
"""

from random import randrange, random
from graphics import *

class MainCharacter:
    """Creates a character to be used as the protagonist in the adventure game"""
    def __init__( self, name, health, regenerations, picture ):
        self.name = name
        self.health = health
        self.regenerations = regenerations
        self.picture = picture
        self.fullHealth = health
        self.startingRegenerations = regenerations
        
    def getName( self ):
        """Returns the name of the main character"""
        return self.name
    
    def getHealth( self ):
        """Returns the health of the main character"""
        return self.health
    
    def getRegenerations( self ):
        """Returns the number of regenerations left of the main character"""
        return self.regenerations
    
    def getPicture( self ):
        """Returns the image file name of the main character"""
        return self.picture
    
    def heroAttacksEnemy( self ):
        """Returns a value to be applied as damage when the main character attacks
           Has a chance to trigger an attack multiplier to the damage. If so, prints
           a notification and amount of the multipler. Then returns multiplied value."""
        characterAttack = randrange(5, 16)
        attackMultiplierChance = random()
        if attackMultiplierChance <= 0.1:
            attackMultiplier = randrange(2,5)
            print('Attack amplified {}x by sonic screwdriver!'.format( attackMultiplier ) )
            characterAttack = characterAttack * attackMultiplier
        return characterAttack
    
    def takeDamage( self, damageInflicted):
        self.health = self.health - damageInflicted
    
    def regenerateHealth( self ):
        self.health = self.fullHealth
        self.regenerations = self.regenerations - 1
        
    def checkHealth( self, eventWindow ):
        if self.getHealth() <= 0 and self.getRegenerations() > 0:
            self.regenerateHealth()
            eventWindow.update('image_regeneration.gif')
            print()
            print('You regenerated! Your health was completely restored,')
            print('but you have a completely new body and personality.')
            print('You have {} regenerations left.'.format( self.getRegenerations() ) )
            input('Hit enter to continue the battle!')
            
        elif self.getHealth() <= 0 and self.getRegenerations() == 0:
            return 'death'
