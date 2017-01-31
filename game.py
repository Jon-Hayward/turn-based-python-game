from character import Character
from monster import Dragon
from monster import Goblin
from monster import Troll
import sys

class Game:
    def setup(self):
        self.player = Character()
        self.monsters = [
          Goblin(),
          Troll(),
          Dragon()
        ]
        self.monster = self.get_next_monster()
    
    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None
    
    def monster_turn(self):
        # check to see if the monster attacks
        if self.monster.attack():
            # if so, tell the player
            print("{} is attacking".format(self.monster))
            
            # check if the player wants to dodge
            if input("Dodge? Y/N ").lower() == 'y':
                # if so, see if the dodge is successful
                if self.player.dodge():
                    # if it is, move on
                    print("You dodged the attack!")
                
                else:
                    print("You got hit anyway!")
                    # if it's not, remove one player hit point
                    self.player.hit_points -= 1
                
            else:
                print("{} hit you for 1 point!".format(self.monster))
                # if it's not, remove one player hit point
                self.player.hit_points -= 1
        else:
            # if the monster isn't attacking, tell that too
            print("{} isn't attacking this turn".format(self.monster))


    def player_turn(self):
        # let the player attack, rest, or quit
        player_choice = input("[A]ttack, [R]est, [Q]uit? ").lower()
        # if they attack:
        if player_choice == "a":
            print("You're attacking {}!".format(self.monster))
            
            if self.player.attack():
                # see if the attack is successful
                if self.monster.dodge():
                    print("{} dodged!".format(self.monster))
                else:
                    if self.player.leveled_up():
                        self.monster.hit_points -= 2
                    else:
                        self.monster.hit_points -= 1
                    # if a good attack, tell the player    
                    print("You hit {} with your {}!".format(self.monster, self.player.weapon))
            else:
                # if not a good attack, tell the player 
                print("You missed!")
        
        # if they rest:
        # call the player.rest() method
        elif player_choice == "r":
            self.player.rest()
        # if they quit, exit the game
        elif player_choice == "q":
            sys.exit()
        # if they pick anything else, re-run this method
        else:
            self.player_turn()
            

    def cleanup(self):
        if self.monster.hit_points <= 0:
            self.player.experiance += self.monster.experiance
            print("You killed {}!".format(self.monster))
            self.monster = self.get_next_monster()

    def __init__(self):
        self.setup()
    
        while self.player.hit_points and (self.monster or self.monsters):
            print("\n" + "="*20)
            print(self.player)
            self.monster_turn()
            print("-"*20)
            self.player_turn()
            self.cleanup()
            print("\n" + "="*20)
            
        if self.player.hit_points:
            print("You win!")
        elif self.monsters or self.monster:
            print("You lose!")
        sys.exit()

Game()