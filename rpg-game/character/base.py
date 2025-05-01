import random
import inspect

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.abilities = []

    def attack(self, opponent):
        if hasattr(opponent, "block_next") and opponent.block_next:
            print(f"{opponent.name} blocks the attack with Divine Shield! No damage taken.")
            opponent.block_next = False
            return

        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")

        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def health_potion(self):
        potions = {
            "Extreme": self.max_health,
            "Super": 50,
            "Ultra": 20,
            "Common": 10
        }

        for potion_type, potion_amount in potions.items():
            print(f"{potion_type} Health Potion: Restores {potion_amount} HP")

        choice = input("Choose a potion to use (1 for Extreme, 2 for Super, 3 for Ultra, 4 for Common): ")

        if choice == '1':
            self.health = self.max_health
            print(f"{self.name} used an Extreme Health Potion and is now at full health!")
        elif choice == '2':
            self.health = min(self.health + 50, self.max_health)
            print(f"{self.name} used a Super Health Potion, restoring 50 HP! Current health: {self.health}")
        elif choice == '3':
            self.health = min(self.health + 20, self.max_health)
            print(f"{self.name} used an Ultra Health Potion, restoring 20 HP! Current health: {self.health}")
        elif choice == '4':
            self.health = min(self.health + 10, self.max_health)
            print(f"{self.name} used a Common Health Potion, restoring 10 HP! Current health: {self.health}")
        else:
            print("Invalid choice! No potion used.")

    def add_ability(self, ability):
        self.abilities.append(ability)

    def use_ability(self, ability_index, opponent):
        if 0 <= ability_index < len(self.abilities):
            ability = self.abilities[ability_index]
            ability(self, opponent)
