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

#marker
time.sleep(1)
# pyautogui.screenshot(r"D:\Desktop\Programming\For_fun\LeagueBot\screenshots\pregame\foo.png", region=lower_half_screen)
# print(pyautogui.locateOnScreen(screenshots_folder + "ingame" + sep + "okay.png", confidence=0.9))
# game_start_setup()
pyautogui.press("q")


"Accept games and sets up champ select"
def start_game():
    find_match()
    pick_champ()
    set_runes()
    choose_summoner_spells()
    wait_until_appears(screenshots_folder + "ingame" + sep + "game_start_score.png", con=0.9)

# "===================[MAIN FUNCTION(S)]==================="
# def play_game(num=1):
#     start_queue()
#     for i in range(num):
#         start_game()
#
# def main():
#     "Starts my bot"
#     initiation()
#     login()
#
#     play_game()
#
#
# if __name__ == "__main__":
#     main()
#     print(">>>>>>>>>[DONE]<<<<<<<<<")
