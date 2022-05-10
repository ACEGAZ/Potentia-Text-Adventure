import time
import random


class Enemy:
    """
    class for all enemies
    """
    def __init__(self, name):
        self.name = name


enemy = Enemy("Sailor")

# Used in part 3 when the player must enter the correct word
PASSWORD = ["Nadaren",
            "nadaren",
            "NADAREN",
            "Nadaren.",
            "nadaren.",
            "NADAREN."
            ]

# Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_D = ["D", "d"]
answer_E = ["E", "e"]
answer_F = ["F", "f"]
answer_G = ["G", "g"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

# race choice for player
RACE_ONE = False
RACE_TWO = False
RACE_THREE = False
RACE_FOUR = False
RACE_FIVE = False
RACE_SIX = False
RACE_SEVEN = False

PLAYER_HEALTH = 10
ENEMY_HEALTH = 8

MELEE_DAMAGE = 2
MAGIC_DAMAGE = 3


def reset_race():
    """
    resets race to false and used when game is restarted
    """
    global RACE_ONE
    RACE_ONE = False
    global RACE_TWO
    RACE_TWO = False
    global RACE_THREE
    RACE_THREE = False
    global RACE_FOUR
    RACE_FOUR = False
    global RACE_FIVE
    RACE_FIVE = False
    global RACE_SIX
    RACE_SIX = False
    global RACE_SEVEN
    RACE_SEVEN = False


def reduce_enemy_health_melee():
    """
    reduces enemy health by 2
    """
    global ENEMY_HEALTH
    ENEMY_HEALTH -= MELEE_DAMAGE


def reduce_player_health_melee():
    """
    reduces player health by 2
    """
    global PLAYER_HEALTH
    PLAYER_HEALTH -= MELEE_DAMAGE


def reduce_enemy_health_magic():
    """
    reduces enemy health by 3
    """
    global ENEMY_HEALTH
    ENEMY_HEALTH -= MAGIC_DAMAGE


def reduce_player_health_magic():
    """
    reduces player health by 3
    """
    global PLAYER_HEALTH
    PLAYER_HEALTH -= MAGIC_DAMAGE


def player_attack_roll():
    """
    returns a random number between 1 and 6 for player melee attack
    """
    while True:
        player_attack = random.randint(1, 6)
        return player_attack


def player_melee_combat():
    """
    player melee combat engine for game
    """
    if RACE_ONE:
        if player_attack_roll() >= 4:
            reduce_enemy_health_melee()
            print("You attack the " + enemy.name + " with your daggers\n"
                  "and hit!\n"
                  "The " + enemy.name + f" has {ENEMY_HEALTH} hit\n" 
                  "points left.\n")
        else:
            print("You missed\n")

    elif RACE_TWO:
        if player_attack_roll() >= 4:
            reduce_enemy_health_melee()
            print(" You swing with your scythe and hit the " + enemy.name +
                  "The " + enemy.name + f" has {ENEMY_HEALTH} hit\n"
                  "points left.\n")
        else:
            print("You missed\n")

    elif RACE_THREE:
        if player_attack_roll() >= 4:
            reduce_enemy_health_melee()
            print(" You crash down your Vasara and hit the " + enemy.name +
                  "The " + enemy.name + f" has {ENEMY_HEALTH} hit\n"
                  "points left.\n")
        else:
            print("You missed\n")

    elif RACE_FOUR:
        if player_attack_roll() >= 4:
            reduce_enemy_health_melee()
            print("You levitate and slash with floating\n"
                  "swords and hit the " + enemy.name +
                  " The " + enemy.name + f" has {ENEMY_HEALTH} hit\n"
                  "points left.\n")
        else:
            print("You missed\n")

    elif RACE_FIVE:
        if player_attack_roll() >= 4:
            reduce_enemy_health_melee()
            print("You slash with your sword and hit the " + enemy.name +
                  " The " + enemy.name + f" has {ENEMY_HEALTH} hit\n"
                  "points left.\n")
        else:
            print("You missed\n")

    elif RACE_SIX:
        if player_attack_roll() >= 4:
            reduce_enemy_health_melee()
            print("You unleash a powerful martial arts strike and hit the\n"
                  + enemy.name +
                  " The " + enemy.name + f" has {ENEMY_HEALTH} hit\n"
                  "points left.\n")
        else:
            print("You missed\n")

    elif RACE_SEVEN:
        if player_attack_roll() >= 4:
            reduce_enemy_health_melee()
            print("You slash with your sharp, metal claws and hit the "
                  + enemy.name +
                  " The " + enemy.name + f" has {ENEMY_HEALTH} hit\n"
                  "points left.\n")
        else:
            print("You missed\n")