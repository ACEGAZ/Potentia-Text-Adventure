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
MAGIK_DAMAGE = 3