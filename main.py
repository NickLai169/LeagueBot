import pyautogui
import time
import os
from functions import *

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

dir_path = os.path.dirname(os.path.realpath(__file__))
sep = os.sep
screenshots_folder = dir_path + sep + "screenshots" + sep
screen_dim = pyautogui.size()

lower_half_screen = (0, int(screen_dim[1]/2), screen_dim[0], int(screen_dim[1]/2))
centre_screen = (int(screen_dim[0]/3), int(screen_dim[1]/3), int(screen_dim[0]/3), int(screen_dim[1]/3))

camera_positions = {1: (1707, 925),
    2: (1714, 948),
    3: (1780, 991),
    4: (1998, 1021)
    }

camps = {
    "b_gromp": [1, (334, 503)],
    "b_blue": [1, (1466, 802)],
    "b_wolves": [2, (1183, 886)],
    "b_chickens": [3, (683, 95)],
    "b_red": [3, (1322, 806)],
    "b_krugs": [4, (1047, 540)],
    }

"""
    [IMPORTANT NOTES]
    # Minimap scale must be at 100%
    # The bot will autoadjust hud to be lowest possible
"""

"logs into the account"
from processes import login

"Set ups a game from the home-screen"
from processes import start_queue

"Finds a match and presses play"
from processes import find_match

"Picks a champion"
from processes import pick_champ

"Sets the runes to the optimal for this strategy"
from processes import set_runes

"Chooses heal and teleport if posible"
from processes import choose_summoner_spells

"Goes into options and sets the necessary startup stuff"
from processes import game_start_setup

"""
Startings looking for a game.
"""
def play_game(num=1):
    print("IAMHERE")
    start_queue()
    for i in range(num):
        start_game()
        break


"Accept games and sets up champ select"
def start_game():
    find_match()
    pick_champ()
    set_runes()
    choose_summoner_spells()
    wait_until_appears(screenshots_folder + "ingame" + sep + "game_start_score.png", con=0.9, wait_duration=300)


# "===================[MAIN FUNCTION(S)]==================="
if __name__ == "__main__":
    play_game()
