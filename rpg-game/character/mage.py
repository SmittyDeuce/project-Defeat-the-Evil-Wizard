from base import Character
import random
import inspect

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=20)  # Boost attack power
        self.abilities = [self.TotalErasure, self.MeteorShower]

    def TotalErasure(self, opponent):
        chance = random.random()
        if self.health <= 5:
            print(f"{self.health} doesn't have enough health for Total Erasure!")
            return
        
        self.health -= 5
        print(f"{self.name} sacrifices 5 health to activate Total Erasure!")
        
        if chance <= 0.08:
            opponent.health = 0
            print(f"{opponent.name} has been completely erased from existence")
        else:
            print(f"Total Erasure fails, {opponent.name} still exists")
            
    def MeteorShower(self, opponent):
        strikes = random.randrange(0, 5)
        total_dmg = strikes * self.attack_power
        opponent.health -= total_dmg
        print(f"{self.name} used Meteor Shower, hitting {strikes} time(s) for a total of {total_dmg} damage!")