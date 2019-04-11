"""
EventWindow Class
    Creates a graphics window with an event image
    
    Methods:
        update - changes the event image to the current event (e.g., enemy, trinket, win, lose)
"""

from graphics import *

class EventWindow:
    """Creates a graphics window with specified image. Image can be updated by event."""
    def __init__( self, title, windowWidth, windowHeight, imagePath):
        self.window = GraphWin( title, windowWidth, windowHeight)
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.imagePath = imagePath
        self.centerPoint = Point( windowWidth / 2, windowHeight / 2)
	
        self.image = Image( self.centerPoint, imagePath )
        self.image.draw( self.window )
    
    def getTitle( self ):
        """Returns the title of the EventWindow object"""
        return self.title
    
    def getWindowWidth( self ):
        """Returns the window width of the EventWindow object"""
        return self.windowWidth
    
    def getWindowHeight( self ):
        """Returns the window height of the EventWindow object"""
        return self.windowHeight
    
    def getImagePath( self ):
        """Returns the image file name of the EventWindow object"""
        return self.imagePath
    
    def update( self, newImagePath ):
        """Changes the image displayed in the EventWindow object to the new image file parameter"""
        self.image.undraw()
        self.image = Image( self.centerPoint, newImagePath )
        self.image.draw( self.window )