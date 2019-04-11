# The Time of the Doctor

'''General Extra Credit Considerations:
    1. Fully-themed game - Dr. Who - but created so that it could easily use other characters/themes
    2. Nearly all concerns encapsulated in their own class, each in their own file,
        leaving a clean, readable main function
    3. Event window updates to current images for each event in game - character, trinkets, enemies, regeneration, winning, losing
    4. Trinkets and enemies are fully themed with sayings/descriptions from the show
    5. Special case if player chooses not to advance a step
    6. Main character has (limited) regeneration feature which refills health when health drops to zero
    7. Extensive (though not full) documentation for the classes and their methods
    8. Every character attack has random damage amount
    9. Every character and enemy attack has small random chance to have attack multiplier
    10.Multiplier for each attack, when activated, is random; gives a text notification of damage amplification
    11.Alternate ending text if regeneration was used
'''

# Import Enemy, Trinket, MainCharacter, Battle, and EventWindow classes
from event_window import EventWindow
from main_character import MainCharacter
from trinket import Trinket
from enemy import Enemy
from battle import Battle

# Many of the functions for moving between games steps
from game_flow_functions import *


def main():
    mainCharacter = MainCharacter( 'The Doctor', 200, 1, 'image_doctors.gif')
    eventWindow = EventWindow( mainCharacter.getName(), 600, 600, mainCharacter.getPicture() )
    gameWelcome( mainCharacter )
    
    # Accumulation variables - I know the trinket counts should be accumulated in a library
    # but I ran out of time to create it and make it work
    stepCount = 0
    bowTieCount = 0
    spoonsCount = 0
    relicCount = 0

    # 10 step game
    while stepCount <= 10:
        
        proceedAnswer = askToProceed( 10 - stepCount)
        # Choosing not to proceed always allows an enemy to catch up to you
        if proceedAnswer == 'n':
            print('An enemy has caught up to you!')
            currentEvent = 'enemy'
        else:
            currentEvent = getEnemyOrTrinket()
               
        if currentEvent == 'trinket':
            # Trinkets for this theme are listed in game_flow_functions right now
            trinket = getTrinketType()
            # Randomly chosen trinket type is used to create an instance of the Trinket class
            currentTrinket = Trinket( trinket[0], trinket[1], trinket[2] )
            bowTieCount, spoonsCount, relicCount = currentTrinket.collect( bowTieCount, spoonsCount, relicCount, eventWindow)   
        else:
            # Enemies for this theme are listed in game_flow_functions right now
            enemy = getEnemyType()
            # Randomly chosen enemy type is used to create an instance of the Enemy class
            currentEnemy = Enemy( enemy[0], enemy[1], enemy[2], enemy[3], enemy[4], enemy[5] )
            # Creates instance of Battle class to handle attacking/damaging events
            currentBattle = Battle( mainCharacter, currentEnemy, eventWindow )
            # Each battle continues until player or enemy has resource (and regenerations) reduced to 0
            currentBattle.battle()
            
        # Check to see if player has been defeated in last battle, else step accumulates and next choice is made
        if mainCharacter.getHealth() <= 0 and mainCharacter.getRegenerations() == 0:
            break
        stepCount += 1
        
    # Once player health and regenerations have been reduced to 0 (lose message)
    # or player has successfully made it through all 10 steps (win message)
    if mainCharacter.getHealth() <= 0 and mainCharacter.getRegenerations() < 1:
        loseMessage( eventWindow)
    else:
        winMessage( eventWindow )
        getStats( mainCharacter.getHealth(), mainCharacter.startingRegenerations, mainCharacter.getRegenerations(), bowTieCount, spoonsCount, relicCount )


main()

