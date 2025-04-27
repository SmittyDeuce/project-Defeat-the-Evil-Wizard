def HealthPotion():
        
        potions = {"Extreme": 1, "Super": 2, "Ultra": 3, "Common": 5}
        for potion_type, potion_amount in potions.items():
            print(f"{potion_type} Health Potion: {potion_amount} ")
        
        use_potion = input("1 for, 2 for ,3 for ")
            
HealthPotion()
