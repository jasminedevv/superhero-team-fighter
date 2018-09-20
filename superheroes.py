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

class Armor:
    def __init__(self, name, defense):
        # Instantiate name and defense strength
        self.name = name
        self.defense = defense

    def defend(self):
        return random.randint(0, self.defense)


class Hero: 
    def __init__(self, name, health=100): 
        self.abilities = list() 
        self.name = name
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def defend(self):
        armor = 0
        for item in self.armors:
            armor += item.defense
        return armor

    def take_damage(self, damage_amt):
        self.health -= damage_amt

    def add_kill(self, num_kills):
        self.kills += num_kills

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

    def add_hero(self, hero):
        print("hero added:", hero.name)
        self.heroes.append(hero)
        print("new hero list:", self.heroes)

    def remove_hero(self, name):
        print("attempting to remove hero:", name)
        if self.heroes == []:
            print("Error: there are no heroes in this list")
            return 0
        for myhero in self.heroes:
            print("made it to the for loop")
            if myhero.name == name:
                print("found hero to remove:", myhero.name)
                self.heroes.remove(myhero)
            else:
                print("hero not found")
                return 0

        """
        Remove hero from heroes list.
        If Hero isn't found return 0.
        """

    def find_hero(self, name):
        print("looking for hero:", name)
        if self.heroes == []:
            print("Error: there are no heroes in this list")
            return 0
        for myhero in self.heroes:
            if myhero.name == name:
                print("hero found:", myhero.name)
                return myhero
            else:
                print("hero not found")
                return 0
        """
        Find and return hero from heroes list.
        If Hero isn't found return 0.
        """

    def view_all_heroes(self):
        for myhero in self.heroes:
            print(myhero.name)

class Arena:
    def __init__(self):
        """
        self.team_one = None
        self.team_two = None
        """

    def build_team_one(self):
        """
        This method should allow a user to build team one.
        """

    def build_team_two(self):
        """
        This method should allow user to build team two.
        """

    def team_battle(self):
        """
        This method should continue to battle teams until 
        one or both teams are dead.
        """

    def show_stats(self):
        """
        This method should print out the battle statistics 
        including each heroes kill/death ratio.
        """

# debug stuff
def debug():
    hero = Hero("Wonder Woman") 
    print(hero.attack()) 
    divine_speed = Ability("Divine Speed", 300) 
    hero.add_ability(divine_speed) 
    print(hero.attack()) 
    new_ability = Ability("Super Human Strength", 800) 
    hero.add_ability(new_ability) 
    print(hero.attack())
    team = Team("One")
    jodie = Hero("Jodie Foster")
    team.add_hero(jodie)
    athena = Hero("Athena")
    team.add_hero(athena)
    print(team.view_all_heroes())

# runs if called directly
if __name__ == "__main__":
    print("I am running in debug mode. Call me from another file to use my classes.")
    debug()