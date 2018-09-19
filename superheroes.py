import random

class Ability: 
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength
        return 1
        # stuff
    def attack(self):
        return 1
        # Return attack value
    def update_attack(self, attack_strength):
        return 1
        # Update attack value

class Weapon(Ability):
    def attack(self):
        """
        This method should should return a random value
        between 0 and the full attack power of the weapon.
        Hint: The attack power is inherited.
        """

class Hero: 
    def init(self, name): 
        self.name = name
        return 1
        # Initialize starting values
    def attack(self):
        return 1
    # Calculate lowest attack value as an integer.
    # Use random.randint(a, b) to select a random attack value.
    # Return attack value between 0 and the full attack.
    def add_ability(self, ability):
        return 1
        # Append ability to self.abilities
    def __init__(self, name): 
        self.abilities = list() 
        self.name = name

class Team:
    def init(self, team_name):
        """Instantiate resources."""
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        return 1
        """Add Hero object to heroes list."""

    def remove_hero(self, name):
        return 1
        """
        Remove hero from heroes list.
        If Hero isn't found return 0.
        """

    def find_hero(self, name):
        return 1
        """
        Find and return hero from heroes list.
        If Hero isn't found return 0.
        """

    def view_all_heroes(self):
        return 1
        """Print out all heroes to the console."""

# Lost functions
random.randint(2, 7)

def debug():
    hero = Hero("Wonder Woman") 
    print(hero.attack()) 
    ability = Ability("Divine Speed", 300) 
    hero.add_ability(ability) 
    print(hero.attack()) 
    new_ability = Ability("Super Human Strength", 800) 
    hero.add_ability(new_ability) 
    print(hero.attack())

if __name__ == "__main__":
    print("I am running in debug mode. Call me from another file to use my classes.")
    debug()