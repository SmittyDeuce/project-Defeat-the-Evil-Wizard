from base import Character
import random
import inspect

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=45)
        self.abilities = [self.FinalStand, self.Blitzkrieg]
        self.blitzkrieg_cooldown = 0  # in turns

    def FinalStand(self, opponent):
        if self.health <= 0:
            print(f"{self.name} is no longer able to fight... Final Stand activates!")
            damage = self.attack_power * 3
            opponent.health -= damage
            print(f"{self.name} deals {damage} damage with Final Stand to {opponent.name}!")
            self.health = 0  # Ensure Warrior stays dead after this move

            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated by Final Stand!")
        else:
            print(f"{self.name} is still alive and cannot use Final Stand.")

    def Blitzkrieg(self, opponent):
        if self.blitzkrieg_cooldown > 0:
            print(f"Blitzkrieg is on cooldown for {self.blitzkrieg_cooldown} more turn(s).")
            return

        rush_attack = self.attack_power
        siphon = rush_attack * 0.09
        opponent.health -= rush_attack
        self.health += siphon
        if self.health > self.max_health:
            self.health = self.max_health

        print(f"{self.name} unleashes Blitzkrieg! A furious charge deals {rush_attack} damage to {opponent.name}!")
        print(f"{self.name} siphons {siphon:.2f} HP. Current HP: {self.health:.2f}/{self.max_health}")

        self.blitzkrieg_cooldown = 3  # Cooldown of 3 turns