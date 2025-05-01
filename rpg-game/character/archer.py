from base import Character
import random
import inspect


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30)
        self.abilities = [self.QuickShot, self.Evade]
        
    def QuickShot(self, opponent):
        damage = self.attack_power + 10
        print(f"{self.name} used Quick Shot! {opponent.name} took {damage} damage!!")
        opponent.health -= damage
        return damage
        
    def Evade(self, opponent=None):
        chance = random.random()
        if chance > 0.5:
            print(f"{self.name} evaded {opponent.name}'s attack!")
            return True
        else:
            print(f"{self.name} failed to evade {opponent.name}'s attack!")
            return False
