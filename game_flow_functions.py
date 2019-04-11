from random import randrange, random
from graphics import *

#Print introduction
def gameWelcome( mainCharacter ): 
    print('Welcome to The Time of {}'.format( mainCharacter.getName() ) )
    print()
    print('You are {}, racing through space and time'.format( mainCharacter.getName() ) )
    print('to save the universe. But first you must save your')
    print('companion, who carries the key to defeating the Daleks')
    print('but is lost in time. Can you reach her before your')
    print('many enemies destroy you and before the Daleks destroy')
    print('all life past, present, and future?')
    print()
    print('You have {0} health points, {1} for each heart, and are'.format( mainCharacter.getHealth(), int( mainCharacter.getHealth() / 2 ) ) )
    print('10 leaps through time and space away from your companion.')
    input('Hit enter and your adventure will begin.')
    
    print()
    
#Get input for step forward (y/n), special instance for the last step!
#   in main(): n = automatic enemy attack (caught from behind), return enemy
#   in main(): y = enemy or trinket
def askToProceed( stepsRemaining ):
    if stepsRemaining == 0:
        print('...........................................')
        print('Oh no, a time attack! That wasn\'t the last leap. It\'s hard to grasp')
        print('this big ball of wibbley-wobbley timey-wimey stuff.')
        proceedAnswer = input('Take the TARDIS on one more leap through time and space (y/n)? ')
        print()
    else:
        print('...........................................')
        proceedAnswer = input('Only {} leaps left. Take the TARDIS on another leap through time and space (y/n)? '.format( stepsRemaining ) )
        print()
        
    while proceedAnswer != 'n' and proceedAnswer != 'y':
        print('You must enter y or n to proceed.')
        proceedAnswer = askToProceed( stepsRemaining)
    return proceedAnswer

#Randomly return an enemy or trinket each step
#Enemies are more interesting than trinkets so higher chance for enemy
def getEnemyOrTrinket():
    enemyOrTrinketChance = random()
    if enemyOrTrinketChance < 0.65:
        enemyOrTrinket = 'enemy'
    else:
        enemyOrTrinket = 'trinket'
    return enemyOrTrinket

#Trinket list holds values for all trinkets, can be expanded infinitely - should have own library for longer lists
def getTrinketType():
    trinketList = [
        ['bow tie', 'Bow ties are cool!', 'image_bowtie.gif'],
        ['new set of spoons', 'See if Ace can hide these from you!', 'image_spoons.gif'],
        ['relic of Gallifrey', 'This may be all that is left of home...', 'image_relic.gif']
        ]
    trinketType = trinketList[ randrange(0, len(trinketList) ) ]
    return trinketType

#Enemy list holds values for all enemies, can be expanded infinitely - should have own library for longer lists
#Previous version used random value to give more challenging enemies lower chances of appearing
#Find a way to combine this with efficiency of library
def getEnemyType():
    enemyList = [
        ['The Silence', 'They are here to ensure your permanent silence.', 32, 'image_silence.gif', 'ancient relgious convictions', 50],
        ['A Weeping Angel', "DON'T BLINK!", 26, 'image_angel.gif', 'time energy', 40],
        ['Lady Cassandra', 'Behold the \'beauty\' of the last surviving human.', 18, 'image_cassandra.gif', 'moisturizers', 10],
        ['The Cybermen', 'Prepare to be upgraded!', 12, 'image_cybermen.gif', 'emotional inhibitors', 30],
        ['A Possessed Ood', 'It has a telepathic field of Basic 100!', 7, 'image_ood.gif', 'connections to the Beast', 20]
        ]
    enemyType = enemyList[ randrange(0, len(enemyList) ) ]
    return enemyType

#Message and image if main character fails
def loseMessage( window ):
    window.update('image_dalek.gif')
    print()
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    print('You were unable to make it to your companion in time.')
    print('She is lost to time and space forever and the Daleks')
    print('begin their intergalactic genocide.')

#Message and image if main character wins
def winMessage( window ):
    window.update('image_tardis.gif')
    print()
    print('*******************************************************')
    print('You rescued your companion and ended the Daleks\'s')
    print('terrible plans. No time to stay for dinner. You are')
    print('off in the TARDIS to the next point in space and time!')
    print()

#Prints out the end game stats - trinkets collected, health remaining, regenerations remaining
def getStats( doctorHealth, regenerations, regenerationsLeft, bowTieCount, spoonsCount, relicCount ):
    print('You set out on your next adventure with {0} health and {1} regeneration remaining.'.format( doctorHealth, regenerationsLeft ) )
    if regenerations - regenerationsLeft == 0:
        print('You did not need to regenerate. You\'re the same ol\' Doctor!')
    else:
        print('You had to regenerate to survive this last adventure.')
        print('You look and act completely different...your companion')
        print('doesn\'t recognize you! Uh oh!')
    print('You have {0} bow ties to wear, {1} sets of spoons to play,'.format( bowTieCount, spoonsCount ) )
    print('and {0} relics from your home planet Gallifrey.'.format( relicCount ) )
