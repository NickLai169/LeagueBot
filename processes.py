import pyautogui
import time
import os

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

dir_path = os.path.dirname(os.path.realpath(__file__))
sep = os.sep
screenshots_folder = dir_path + sep + "screenshots" + sep
screen_dim = pyautogui.size()

lower_half_screen = (0, int(screen_dim[1]/2), screen_dim[0], int(screen_dim[1]/2))
centre_screen = (int(screen_dim[0]/3), int(screen_dim[1]/3), int(screen_dim[0]/3), int(screen_dim[1]/3))



"sensor function determining the mouse position"
from functions import mouseposition

"clicks the image if it's there, does nothing  if it's not"
from functions import click_image

"""Waits until the specified image appears on screen, throws exception
if image not found within specified duration (or time up)"""
from functions import wait_until_appears

"""Waits until the one of the images in the image_lst appears, does
not throw any exceptions"""
from functions import wait_until_one_appears

"Function checking whether and image appeared on screen within indicated duration"
from functions import check_if_appears



"[[[[PROCESSES]]]]"

"just a small indicator thing to show that the script is beginning"
def initiation():
    print("Starting bot")
    time.sleep(0.5)
    for i in range(1,4):
        print(4-i)
        time.sleep(1)
    print("BEGIN!")

"""logs into the account
    @param username: username of the account we're trying to log into
    @param password: passwrod of the account we're trying to log into
"""
def login(username="lamaboti", password="iamabot1"):
    "Opens up league of legends"
    click_image(screenshots_folder + "pregame" + sep + "windows_start_logo.png")
    pyautogui.write("League of Legends")
    for i in range(10):
        if check_if_appears(screenshots_folder + "pregame" + sep + "league_start_menu.PNG", con=0.7):
            break;
        print("====> finding league logo...")
        time.sleep(0.5)
    click_image(screenshots_folder + "pregame" + sep + "league_start_menu.PNG")

    "logs in"
    pyautogui.PAUSE = 0.05
    print("====> logging in...")
    username_loc = None
    for i in range(20):
        username_loc = pyautogui.locateCenterOnScreen(screenshots_folder + "pregame" + sep + "login_username1.PNG", confidence=0.9)
        if username_loc:
            break;
        username_loc = pyautogui.locateCenterOnScreen(screenshots_folder + "pregame" + sep + "login_username2.PNG", confidence=0.9)
        if username_loc:
            break;
        time.sleep(0.5)

    if not username_loc:
        print(username_loc)
        raise Exception("username bar not found/covered")
    pyautogui.click(username_loc)

    print("====> typing Username and password...")
    pyautogui.write(username)
    click_image(screenshots_folder + "pregame" + sep + "login_password.png")
    pyautogui.write(password)
    click_image(screenshots_folder + "pregame" + sep + "enter_league.png")

    pyautogui.PAUSE = 0.1

    for i in range(30):
        print("====> waiting for Play button(s)...")
        play_button = pyautogui.locateCenterOnScreen(screenshots_folder + "pregame" + sep + "loginPLAY_button.png", confidence=0.5)
        if play_button:
            print("====> found large PLAY button")
            pyautogui.click(play_button)
            break;
        play_button = pyautogui.locateCenterOnScreen(screenshots_folder + "pregame" + sep + "play_button.png", confidence=0.5)
        if play_button:
            print("====> large PLAY button omitted")
            break;
        time.sleep(1)


"Set ups a game from the home-screen"
def start_queue():
    print("====> setting up queue...")
    "Clicks the play/party button in the top-right"
    wait_until_appears(screenshots_folder + "pregame" + sep + "play_button.png", con=0.9, wait_duration=40)
    start_button = pyautogui.locateCenterOnScreen(screenshots_folder + "pregame" + sep + "play_button.png")

    if not start_button:
        start_button = pyautogui.locateCenterOnScreen(screenshots_folder + "pregame" + sep + "party_play_button.png")
    pyautogui.click(start_button)

    find_match_button = screenshots_folder + "pregame" + sep + "find_match_button.png"
    confirm_match = screenshots_folder + "pregame" + sep + "confirm_button.png"
    wait_until_one_appears([find_match_button, confirm_match], wait_duration=20, con=0.9, reg=lower_half_screen)

    "selects co-op vs AI and starts queue"
    co_op_v_ai_loc = pyautogui.locateCenterOnScreen(screenshots_folder + "pregame" + sep + "co_op_v_ai.PNG")
    if not co_op_v_ai_loc:
        click_image(screenshots_folder + "pregame" + sep + "co_v_ai.png")

    click_image(screenshots_folder + "pregame" + sep + "intro_bots.PNG", con=0.9)

"Finds a match and presses play"
def find_match():
    print("====> starting queue...")
    click_image(screenshots_folder + "pregame" + sep + "confirm_button.png")
    pyautogui.moveTo(960, 540)
    time.sleep(3)
    wait_until_appears(screenshots_folder + "pregame" + sep + "find_match_button.png", con=0.5)
    click_image(screenshots_folder + "pregame" + sep + "find_match_button.png", con=0.5)
    wait_until_appears(screenshots_folder + "pregame" + sep + "accept_button.png", wait_duration=40, con=0.9)
    spot = click_image(screenshots_folder + "pregame" + sep + "accept_button.png", con=0.9)
    print("Accept button located at: " + str(spot))
    if spot:
        print("====> Match accepted...")
    else:
        raise Exception("Accept button not clicked")

    lock_in_button = screenshots_folder + "champ_select" + sep + "lock_in(grey).png"
    in_queue = screenshots_folder + "pregame" + sep + "in_queue.png"
    pyautogui.screenshot(r"" + screenshots_folder + "pregame" + sep + "centre_screen.png", region=centre_screen)
    middle_of_screen = screenshots_folder + "pregame" + sep + "centre_screen.png"

    wait_until_one_appears([lock_in_button, middle_of_screen], con=0.9, wait_duration=60, reg=lower_half_screen)
    if pyautogui.locateOnScreen(in_queue, confidence=0.9, region= lower_half_screen):
        print("====> Some fuckwit declined (ಠ ∩ಠ)")
        find_match()
    elif not pyautogui.locateOnScreen(lock_in_button, confidenceq=0.9, region= lower_half_screen):
        raise Exception("Something went wrong during queue-time!")

"Picks a champion"
def pick_champ():
    print("====> Selecting champion...")
    wait_until_appears(screenshots_folder + "champ_select" + sep + "lock_in(grey).png", con=0.8)
    lock_in_loc = pyautogui.locateCenterOnScreen(screenshots_folder + "champ_select" + sep + "lock_in(grey).png", confidence=0.8)
    click_image(screenshots_folder + "champ_select" + sep + "adc_role.png", 0.8)
    time.sleep(0.2)
    for i in range(1, 20):
        print("Looking at champion " + str(i))
        select_champ = pyautogui.locateCenterOnScreen(screenshots_folder + "champ_select" + sep + str(i) + ".png", confidence=0.8)
        if select_champ:
            pyautogui.click(select_champ)
            time.sleep(1)
            pyautogui.click(lock_in_loc)
            time.sleep(1)
            if not pyautogui.locateCenterOnScreen(screenshots_folder + "champ_select" + sep + "lock_in(blue).png", confidence=0.8):
                print("Locked in champion " + str(i))
                break;
"Sets the runes to the optimal for this strategy"
def set_runes():
    time.sleep(1)
    editloc = pyautogui.locateCenterOnScreen(screenshots_folder + "champ_select" + sep + "edit_runes.png", confidence=0.8)
    if editloc:
        pyautogui.click(editloc)
        if not pyautogui.locateOnScreen(screenshots_folder
        + "champ_select" + sep + "correct_runes.png", confidence=0.945):
            pyautogui.PAUSE = 0.05
            time.sleep(0.5)
            pyautogui.move(-screen_dim[0]/10, -screen_dim[1]*8/15)
            pyautogui.click()
            pyautogui.move(screen_dim[0]/20, screen_dim[1]*2/17)
            pyautogui.click()
            pyautogui.move(-screen_dim[0]/40, screen_dim[1]/7)
            pyautogui.click()
            pyautogui.move(screen_dim[0]/28, screen_dim[1]/11)
            pyautogui.click()
            pyautogui.move(-screen_dim[0]/35, screen_dim[1]/11)
            pyautogui.click()
            pyautogui.move(screen_dim[0]*2/13, -screen_dim[1]*7/16)
            pyautogui.click()
            pyautogui.move(screen_dim[0]/80, screen_dim[1]/11)
            pyautogui.click()
            pyautogui.move(screen_dim[0]/12, screen_dim[1]/13)
            pyautogui.click()
            pyautogui.move(-screen_dim[0]/22, screen_dim[1]/6)
            pyautogui.click()
            pyautogui.move(-screen_dim[0]/25, screen_dim[1]/17)
            pyautogui.click()
            pyautogui.move(screen_dim[0]/25, screen_dim[1]/18)
            pyautogui.click()
            click_image(screenshots_folder + sep + "champ_select" + sep + "save_runes.png", con=0.9)
            pyautogui.PAUSE = 0.1
        click_image(screenshots_folder + "champ_select" + sep + "exit_rune_page.png", con=0.9)
        click_image(screenshots_folder + "champ_select" + sep + "yes.png", con=0.9)

"Chooses heal and teleport if posible"
def choose_summoner_spells():
    pyautogui.PAUSE = 0.05
    "opens up summoner_spell_1 selection"
    emotes_icon = pyautogui.locateCenterOnScreen(screenshots_folder + "champ_select" + sep + "emotes_icon_2.png", confidence=0.9)
    print(emotes_icon)
    pyautogui.moveTo(emotes_icon)
    pyautogui.move(-screen_dim[0]*1/10, 0)
    pyautogui.click()

    "selects heal"
    time.sleep(0.5)
    mouse_pos_1 = pyautogui.position()
    summoner_spell_region = (int(mouse_pos_1[0] - screen_dim[0]/12), int(mouse_pos_1[1] - screen_dim[1]/3)
        , int(screen_dim[0]/5), int(screen_dim[1]/4))
    print(summoner_spell_region)
    select_heal_pos = pyautogui.locateCenterOnScreen(screenshots_folder
        + "champ_select" + sep + "heal.png", confidence=0.9, region=summoner_spell_region)
    pyautogui.click(select_heal_pos)

    "selects teleport (if possible)"
    time.sleep(0.5)
    pyautogui.moveTo(mouse_pos_1)
    pyautogui.move(screen_dim[0]/33, 0)
    pyautogui.click()
    time.sleep(0.5)
    select_teleport_pos = pyautogui.locateCenterOnScreen(screenshots_folder
        + "champ_select" + sep + "teleport.png", confidence=0.9, region=summoner_spell_region)
    pyautogui.click(select_teleport_pos)

"Goes into options and sets the necessary startup stuff"
def game_start_setup():
    "Sets all to smartcast"
    pyautogui.PAUSE = 0.05
    click_image(screenshots_folder + "ingame" + sep + "settings.png", con=0.9)
    print("click settings")

    click_image(screenshots_folder + "ingame" + sep + "hotkeys.png", con=0.9)
    print("click hotkeys")

    click_image(screenshots_folder + "ingame" + sep + "quick_cast_all.png", con=0.9)
    print("click quick_cast_all")
    print("set all to smartcast")

    "sets interface to minimal hud"
    click_image(screenshots_folder + "ingame" + sep + "interface.png", con=0.9)
    pyautogui.moveTo((pyautogui.position()[0] + screen_dim[0]/10, pyautogui.position()[1]))
    for i in range(20):
        pyautogui.scroll(100)
        time.sleep(0.1)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    pyautogui.drag(-1*pyautogui.position()[0]*1/12, 0, 0.5, button="left")

time.sleep(2)
game_start_setup()
