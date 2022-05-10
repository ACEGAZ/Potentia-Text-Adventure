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


def player_magic_roll():
    """
    returns a random number between 1 and 6 for player magic attack
    """
    while True:
        player_magic = random.randint(1, 6)
        return player_magic


def player_magic_combat():
    """
    player magic combat engine for game
    """
    if RACE_ONE:
        if player_magic_roll() >= 5:
            reduce_enemy_health_magic()
            print("You send a jet of water flying at the " + enemy.name +
                  " and hit!\n"
                  " The " + enemy.name + f" has {ENEMY_HEALTH} hit\n"
                  "points left.\n")
        else:
            print("Your Aqua magic misses\n")

    elif RACE_TWO:
        if player_magic_roll() >= 5:
            reduce_enemy_health_magic()
            print("You send shards of ice flying at the " + enemy.name +
                  " and hit!\n"
                  "The " + enemy.name + f" has {ENEMY_HEALTH} hit\n"
                  "points left.\n")
        else:
            print("Your Cryo magic misses\n")

    elif RACE_THREE:
        if player_magic_roll() >= 5:
            reduce_enemy_health_magic()
            print("You send a fireball flying at the " + enemy.name +
                  " and hit!\n"
                  "The " + enemy.name + f" has {ENEMY_HEALTH} hit\n"
                  "points left.\n")
        else:
            print("Your Pyro magic misses\n")

    elif RACE_FOUR:
        if player_magic_roll() >= 5:
            reduce_enemy_health_magic()
            print("You send a blast of wind towards the " + enemy.name +
                  " and hit!\n"
                  "The " + enemy.name + f" has {ENEMY_HEALTH} hit\n"
                  " points left.\n")
        else:
            print("Your zephyr magic misses\n")

    elif RACE_FIVE:
        if player_magic_roll() >= 5:
            reduce_enemy_health_magic()
            print("You drain some of the " + enemy.name + "soul!"
                  "The " + enemy.name + f" has {ENEMY_HEALTH} hit\n"
                  "points left.\n")
        else:
            print("Your Soul magic misses\n")

    elif RACE_SIX:
        if player_magic_roll() >= 5:
            reduce_enemy_health_magic()
            print("You send a chunk of rock flying towards the "
                  + enemy.name + " and hit!\n"
                  "The " + enemy.name + f" has {ENEMY_HEALTH} hit\n"
                  "points left.\n")
        else:
            print("Your Terra magic misses\n")

    elif RACE_SEVEN:
        if player_magic_roll() >= 5:
            reduce_enemy_health_magic()
            print("You send a bolt of lightning flying at the " + enemy.name +
                  " and hit!\n"
                  "The " + enemy.name + f" has {ENEMY_HEALTH} hit\n"
                  "points left.\n")
        else:
            print("Your Fulgeration magic misses\n")


def enemy_attack_roll():
    """
    returns a random number between 1 and 6 for enemy melee attack
    """
    while True:
        enemy_attack = random.randint(1, 6)
        return enemy_attack


def enemy_melee_combat():
    """
    enemy melee combat engine for game
    """

    print("The " + enemy.name + " tries to melee attack you\n")
    time.sleep(2)
    if enemy_attack_roll() >= 3:
        reduce_player_health_melee()
        print("The " + enemy.name + " hit you with a melee attack!"
              f" You have {PLAYER_HEALTH} hit points left""\n")
        time.sleep(2)
    else:
        print("The " + enemy.name + " missed you with its melee attack\n")
        time.sleep(2)


def enemy_magic_roll():
    """
    returns a random number between 1 and 6 for enemy magic attack
    """
    while True:
        enemy_magic = random.randint(1, 6)
        return enemy_magic


def enemy_magic_combat():
    """
    computer magic combat engine for game
    """
    print("The " + enemy.name + " tries to hit you with a magic attack\n")
    time.sleep(2)
    if enemy_magic_roll() >= 5:
        reduce_player_health_magic()
        print("The " + enemy.name + " hit you with a magic attack!"
              f" You have {PLAYER_HEALTH} hit points left""\n")
        time.sleep(2)
    else:
        print("The enemy missed you with its magic attack\n")
        time.sleep(2)


def enemy_attack_choice_roll():
    """
    returns a random number between 1 and 6 for enemy attack choice
    """
    while True:
        enemy_attack_or_magic_choice_generator = random.randint(1, 6)
        return enemy_attack_or_magic_choice_generator


def enemy_attack_choice():
    """
    decides which attack the enemy will use.
    """
    if enemy_attack_choice_roll() <= 4:
        enemy_melee_combat()
    elif enemy_attack_choice_roll() >= 5:
        enemy_magic_combat()


def combat_encounter():
    """
    runs combat until enemy or player is dead
    """
    global PLAYER_HEALTH
    global ENEMY_HEALTH
    while ENEMY_HEALTH > 0 or PLAYER_HEALTH > 0:
        print("A: melee attack\n"
              "B: magic attack\n")
        choice = input(">>>  ")
        if choice in answer_A:
            player_attack_roll()
            player_melee_combat()
            time.sleep(2)
        elif choice in answer_B:
            player_magic_roll()
            player_magic_combat()
            time.sleep(2)
        else:
            print("Please enter a valid input\n")
            time.sleep(2)
            combat_encounter()

        if ENEMY_HEALTH > 0:
            enemy_attack_roll()
            enemy_magic_roll()
            enemy_attack_choice_roll()
            enemy_attack_choice()
        elif ENEMY_HEALTH <= 0:
            print("You defeated the " + enemy + "\n")
            time.sleep(2)
            PLAYER_HEALTH = 10
            ENEMY_HEALTH = 8
            print("Your hit points have been restored.\n"
                  f"You have {PLAYER_HEALTH} hit points\n"
                  "\n")
            break

        if PLAYER_HEALTH <= 0:
            PLAYER_HEALTH = 10
            ENEMY_HEALTH = 8
            print("You Died!")
            time.sleep(2)
            start_menu()