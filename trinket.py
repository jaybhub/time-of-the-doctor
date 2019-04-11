"""
Trinket Class
    Trinket object created randomly from list in adventure game
    
    Method:
        collect - prints out name and description of trinket
                  updates event window with image of trinket
                  accumulates each trinket type in accumulation variable
"""

from graphics import *

class Trinket:
    """Creates a trinket to be collected by the main character in the adventure"""
    def __init__( self, name, description, picture ):
        self.name = name
        self.description = description
        self.picture = picture
        
    def getName( self ):
        """Returns the name of the trinket"""
        return self.name
    
    def getDescription( self ):
        """Returns the description of the trinket"""
        return self.description
    
    def getPicture( self ):
        """Returns the image file name of the trinket"""
        return self.picture

    def collect( self, bowTieCount, spoonsCount, relicCount, eventWindow ):
        """Updates the event window with a picture of the trinket.
           Prints out the name and description of the trinket.
           Accumulates the trinket type counts over the course of the adventure.""" 
        eventWindow.update( self.getPicture() )
        
        print('You found a {0}! {1}'.format( self.getName(), self.getDescription() ) )
        print()
        
        if self.getName() == 'bow tie':
            bowTieCount += 1
        elif self.getName() == 'new set of spoons':
            spoonsCount += 1
        else:
            relicCount += 1
            
        input('Hit enter to continue')
        return bowTieCount, spoonsCount, relicCount