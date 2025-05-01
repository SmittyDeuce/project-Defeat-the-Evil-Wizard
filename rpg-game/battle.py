import inspect
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
            for index, ability in enumerate(player.abilities):
                print(f"{index + 1}. {ability.__name__.replace('_', ' ').capitalize()}")

            ability_used = int(input("Choose an ability: "))
            if 1 <= ability_used <= len(player.abilities):
                selected_ability = player.abilities[ability_used - 1]
                
                params = inspect.signature(selected_ability).parameters
                
                if len(params) > 1:
                    selected_ability(player, wizard)
                else:
                    selected_ability(wizard)
                
            else:
                print("Invalid ability choice")
                    
        elif choice == '3':
            player.HealthPotion()
            
        elif choice == '4':
            player.display_stats()
            
        else:
            print("Invalid choice, try again.")
            continue
        
        if isinstance(player, Warrior) and player.blitzkrieg_cooldown > 0:
            player.blitzkrieg_cooldown -= 1

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"{wizard.name} has been defeated by {player.name}!")