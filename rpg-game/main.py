from character.character_creater import create_character
from enemies.evil_wizard import EvilWizard
from battle import battle

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()