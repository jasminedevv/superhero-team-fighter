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
        return random.randint(0, self.attack_strength)

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
        print(self.name, "has taken", damage_amt, "damage")
        if self.health <= 0:
            print(self.name, "has fallen!")
            self.deaths += 1
            print(self.deaths)

    def add_kill(self, num_kills):
        self.kills += num_kills

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_ability(self, ability):
        self.abilities.append(ability)
        # Append ability to self.abilities

    def add_armor(self, armor):
        self.armors.append(armor)



class Team:
    def __init__(self, team_name):
        """Instantiate resources."""
        self.name = team_name
        self.heroes = list()
        # self.deaths = 0

    def defend(self, damage):
        dps = damage / len(self.heroes)
        deaths = 0
        for hero in self.heroes:
            hero.health -= (dps - hero.defend())
            if hero.health <= 0:
                deaths += 1
        return deaths

    def attack(self, opposing_team):
        total_damage = 0
        for hero in self.heroes:
            total_damage += hero.attack()
        dps = total_damage / len(opposing_team.heroes)
        our_kills = 0
        for hero in opposing_team.heroes:
            hero.take_damage(dps)
            if hero.deaths > 0:
                our_kills += 1
        for hero in self.heroes:
            hero.kills += our_kills
        return total_damage

    def revive_heroes(self):
        for hero in self.heroes:
            hero.health = 60

    def add_hero(self, hero):
        print("\nhero added:", hero.name)
        self.heroes.append(hero)
        # print("\nnew hero list:", self.heroes)

    def remove_hero(self, name):
        print("attempting to remove hero:", name)
        if self.heroes == []:
            print("\nError: there are no heroes in this list")
            return 0
        for myhero in self.heroes:
            if myhero.name == name:
                print("\nfound hero to remove:", myhero.name)
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
            print("\nError: there are no heroes in this list")
            return 0
        for myhero in self.heroes:
            if myhero.name == name:
                print("\nhero found:", myhero.name)
                return myhero
            else:
                print("\nhero not found")
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
        self.team_one = list()
        self.team_two = list()

    def build_team_one(self):
        self.team_one = Team("Red Team")
        # print("Build your team! Choose wisely from the following list. You get 3 heroes.")
        # this is some top shit code below
        # note: make more DRY and plan for user messing up multiple times
        # print(available_heroes_string)
        # choice1 = input("Your First Choice > ")
        # if choice1 not in available_heroes_string:
        #     choice1 = input("That is not an option. Please try again > ")
        # choice2 = input("Your Second Choice > ")
        # if choice2 not in available_heroes_string:
        #     choice1 = input("That is not an option. Please try again > ")
        # choice3 = input("Your Third Choice > ")
        # if choice3 not in available_heroes_string:
        #     choice3 = input("That is not an option. Please try again > ")
        # self.team_one.append(choice1)
        # self.team_one.add_hero(choice2)
        # self.team_one.add_hero(choice3)
        # print("You have chosen", choice1, "as your hero.")
        """
        This method should allow a user to build team one.
        """

    def build_team_two(self):
        self.team_two = Team("Blue Team")
        # why do these have to be different functions that makes no sense
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
    # debug()