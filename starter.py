import random
# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def HealthPotion(self):
        potions = {
            "Extreme": self.max_health,  # Full health restore
            "Super": 50,  # Restores 50 health points
            "Ultra": 20,   # Restores 20 health points
            "Common": 10   # Restores 10 health points
        }
        
        # Display available potions and their healing values
        for potion_type, potion_amount in potions.items():
            print(f"{potion_type} Health Potion: Restores {potion_amount} HP")
        
        # Ask the user to choose a potion
        choice = input("Choose a potion to use (1 for Extreme, 2 for Super, 3 for Ultra, 4 for Common): ")

        if choice == '1':
            # Extreme Potion: Restores full health
            self.health = self.max_health
            print(f"{self.name} used an Extreme Health Potion and is now at full health!")
        elif choice == '2':
            # Super Potion: Restores 50 health
            if self.health + 50 > self.max_health:
                self.health = self.max_health
            else:
                self.health += 50
            print(f"{self.name} used a Super Health Potion, restoring 50 HP! Current health: {self.health}")
        elif choice == '3':
            # Ultra Potion: Restores 20 health
            if self.health + 20 > self.max_health:
                self.health = self.max_health
            else:
                self.health += 20
            print(f"{self.name} used an Ultra Health Potion, restoring 20 HP! Current health: {self.health}")
        elif choice == '4':
            # Common Potion: Restores 10 health
            if self.health + 10 > self.max_health:
                self.health = self.max_health
            else:
                self.health += 10
            print(f"{self.name} used a Common Health Potion, restoring 10 HP! Current health: {self.health}")
        else:
            print("Invalid choice! No potion used.")
            

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=45)  # Boost health and attack power

    def FinalStand(self, opponent):
        if self.health <= 0:
            print(f"{self.name} is no longer able to fight... Final Stand activates!")
            # Here, you can calculate the damage for Final Stand.
            damage = self.attack_power * 3  # Example damage calculation
            opponent.health -= damage
            print(f"{self.name} deals {damage} damage with Final Stand to {opponent.name}!")
            self.health = 0  # Ensure health is set to 0 after Final Stand activates.
        else:
            print(f"{self.name} takes damage! Remaining health: {self.health}")

    def Blitzkrieg(self, opponent):
        print(f"{self.name} uses Blitzkrieg! Hurling an axe imbued with lightning, causing paralysis!")
        print(f"{opponent.name} will miss their next turn due to the paralysis!")

        


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=20)  # Boost attack power

    def TotalErasure(self, opponent):
        chance = random.random()
        if self.health <= 5:
            print(f"{self.health} doesnt have enough health for Total Erasure!")
            return
        
        self.health -= 5
        print(f"{self.name} sacrifices 5 health to activate Total Erasure!")
        
        if chance <= 0.08:
            opponent.health = 0
            print(f"{opponent.name} has been completely erased from existence")
            
        else:
            print(f"Total Erasure fails, {opponent.name} still exists")
            
    def MeteorShower(self):
        strikes = random.randrange(0, 5)
        total_dmg = strikes * self.attack_power

        print(f"{self.name} used Meteor Shower, hitting {strikes} time(s) for a total of {total_dmg} damage!")
        return total_dmg
        
            
    
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30)
        
    def QuickShot(self):
        damage = self.attack_power + 10
        print(f"{self.name} used Quick Shot for {damage} damage!!")
        return damage
        
    def Evade(self):
        chance = random.random()
        
        if chance > 0.5:
            print(f"{self.name} evaded the Attack!")
            return True
        else:
            print(f"{self.name} failed to evade!")
            return False
        

class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=35)
        
    def HolyStrike(self):
        crit_attack = 2
        holy_damage = 5
        chance = random.random()
        
        if chance < 0.7:
            total_damage = (self.attack_power + holy_damage) * crit_attack
            print(f"{self.name} used HolyStrike! It hit critically for {total_damage} damage!")
            return total_damage
        else:
            total_damage = self.attack_power + holy_damage
            print(f"{self.name} used HolyStrike for {total_damage} damage.")
            return total_damage
        
    def DivineShield(self):
        print(f"{self.name} activates Divine Shield! Next attack will be blocked.")
        return True
            
        
            


# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  # Lower attack power
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")  # Add Archer
    print("4. Paladin")  # Add Paladin
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            # Call the special ability here
            pass  # Implement this
        elif choice == '3':
            # Call the heal method here
            pass  # Implement this
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()
    