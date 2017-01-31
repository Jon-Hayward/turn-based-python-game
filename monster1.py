from combat import Combat

import random

COLORS = ["yellow", "green", "red", "white", "black", "shiny"]


class Monster(Combat):
    min_hit_points = 1
    max_hit_points = 1
    min_experiance = 1
    max_experiance = 1
    weapon = "sword"
    sound = "roar"
    
    def __init__(self, **kwargs):
        self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
        self.experiance = random.randint(self.min_experiance, self.max_experiance)
        self.color = random.choice(COLORS)
        
        for key, value in kwargs.items():
            setattr(slef, key, value)
    
    def battlecry(self):
        return self.sound.upper()
    
    def __str__(self):
        return "{} {} HP: {}, XP {}".format(self.color.title(),
                                            self.__class__.__name__,
                                            self.hit_points,
                                            self.experiance)
    
    
    
class Goblin(Monster):
    max_hit_points = 3
    max_experiance = 2 
    sound = "squeak"
    
class Troll(Monster):
    min_hit_points = 3
    max_hit_points = 5
    min_experiance = 2
    max_experiance = 6
    sound = "growl"
    
class Dragon(Monster):
    min_hit_points = 5
    max_hit_points = 10
    min_experiance = 6
    max_experiance = 10
    sound = "roar"