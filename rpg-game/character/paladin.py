from .base import Character
import random

class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=35)
        self.abilities = [self.HolyStrike, self.DivineShield]
        self.block_next = False
        
    def HolyStrike(self, opponent):
        crit_attack = 2
        holy_damage = 5
        chance = random.random()
        
        if chance < 0.7:
            total_damage = (self.attack_power + holy_damage) * crit_attack
            print(f"{self.name} used HolyStrike! It hit critically for {total_damage} damage!")
        else:
            total_damage = self.attack_power + holy_damage
            print(f"{self.name} used HolyStrike for {total_damage} damage.")
        
        opponent.health -= total_damage
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
        
    def DivineShield(self, opponent=None):
        self.block_next = True
        print(f"{self.name} activates Divine Shield! The next attack will be blocked.")