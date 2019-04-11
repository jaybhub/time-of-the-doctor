"""
battle - the entire interaction between main character and enemy instance
         updates event window to show enemy
         iterates until character or enemy resource is depleted
         prints notification of each attack/damage by both combatants
         ends when one combatant dies
         allows for main character regeneration
         prints notifications of defeat and regenerations, updates event window image
"""

from graphics import *

class Battle:
    def __init__( self, hero, enemy, eventWindow ):
        self.hero = hero
        self.enemy = enemy
        self.eventWindow = eventWindow
        
    def battle( self ):
        """Updates the event window with a picture of the enemy. Prints the name, description, resource,
           and resource amount for this enemy. Iterates through a battle with the main character until
           the enemy or main character have their resource and regenerations reduced to 0.
           Main character attacks first. If enemy is not defeated, enemy attacks next. Then repeats. Allows
           for main character regeneration, prints out notification and updates image.
           If enemy is defeated, prints notification and returns remaining health and regenerations for
           main character. If main character is defeated, breaks out of loop and returns character health (0)
           and regenerations (0)."""
         
        self.eventWindow.update(self.enemy.getPicture())
    
        print('You exit the Tardis to face an enemy.')
        print("It's {0}! {1}".format( self.enemy.getName(), self.enemy.getDescription() ) )
        print('You need to take away {0} {1} to win this battle.'.format( self.enemy.getResourceAmount(), self.enemy.getResourceName() ) )
        print()
    
        while self.enemy.getResourceAmount() > 0:
            currentAttack = self.hero.heroAttacksEnemy()
            self.enemy.takeDamage( currentAttack )
            
            print('You attack!')
            print('{0} loses {1} {2}. {3} {2} remaining.'.format( self.enemy.getName(), currentAttack, self.enemy.getResourceName(), self.enemy.getResourceAmount() ) )
        
            if self.enemy.getResourceAmount() <= 0:
                print('{} defeated!'.format( self.enemy.getName() ) )
                break
        
            else:
                print()
                print('{} is attacking you!'.format( self.enemy.getName() ) )
                
                enemyAttack = self.enemy.enemyAttacksHero()
                self.hero.takeDamage( enemyAttack )
                
                print('You lose {0} health points. {1} health points remaining.'.format( enemyAttack, self.hero.getHealth() ) )

                healthCheck = self.hero.checkHealth( self.eventWindow )
                if healthCheck == 'death':
                    break
                else:
                    print('-------------------')
                    input('Hit enter to attack again.')
                    print()
                        
                self.eventWindow.update( self.enemy.getPicture() )
                