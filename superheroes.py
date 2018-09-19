import random

class Ability: 
    def __init__(self, name, attack_strength):
        # example: Big Strength
        self.name = name
        # example: 300
        self.attack_strength = attack_strength
    def attack(self):
        min_attack = self.attack_strength // 2
        max_attack = self.attack_strength
        return random.randint(min_attack, max_attack)
    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength
        # Update attack value

class Weapon(Ability):
    def attack(self):
        """
        This method should should return a random value
        between 0 and the full attack power of the weapon.
        Hint: The attack power is inherited.
        """
        # i've got the sneaking suspicion this is one simple ass line of code like this
        return random.randint(0, self.attack_strength)
        # well it passes but idk where it's pulling attack_strength from

class Hero: 
    def __init__(self, name): 
        self.abilities = list() 
        self.name = name

        # Initialize starting values
    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
    def add_ability(self, ability):
        # no idea why this works
        self.abilities.append(ability)
        # Append ability to self.abilities

class Team:
    def __init__(self, team_name):
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
    divine_speed = Ability("Divine Speed", 300) 
    hero.add_ability(divine_speed) 
    print(hero.attack()) 
    new_ability = Ability("Super Human Strength", 800) 
    hero.add_ability(new_ability) 
    print(hero.attack())

if __name__ == "__main__":
    print("I am running in debug mode. Call me from another file to use my classes.")
    debug()