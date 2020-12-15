import pyautogui
import pydirectinput
import time
import os
import sys
from functions import *
import winsound
import ctypes
import random

from pynput.mouse import Button, Controller
Mouse = Controller

from pynput.keyboard import Key, Controller
Keyboard = Controller


pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

dir_path = os.path.dirname(os.path.realpath(__file__))
sep = os.sep
screenshots_folder = dir_path + sep + "screenshots" + sep
screen_dim = pyautogui.size()

lower_half_screen = (0, int(screen_dim[1]/2), screen_dim[0], int(screen_dim[1]/2))
centre_screen = (int(screen_dim[0]/3), int(screen_dim[1]/3), int(screen_dim[0]/3), int(screen_dim[1]/3))

"""
[Helper functions]
"""
def do_wolves(t=160):
    # Note, this function requires unlock screen to work properly
    frequency = 440  # Set Frequency To 2500 Hertz
    duration = 300  # Set Duration To 1000 ms == 1 second

    while True:
        winsound.Beep(frequency, duration)
        time.sleep(0.2)
        winsound.Beep(frequency, duration)
        time.sleep(1)
        print("Doing wolves...")
        tabbed_in = tab_into_league()

        time.sleep(0.5)
        pyautogui.PAUSE = 0.25
        original_pos = pyautogui.position()
        pyautogui.click(x=1714, y=948, button='left')
        pyautogui.moveTo(1183, 886)
        pyautogui.click(x=1183, y=886, button='right')

        pyautogui.PAUSE = 0.05
        alt_tab(tabbed_in)

        pyautogui.moveTo(original_pos)
        pyautogui.PAUSE = 0.5
        time.sleep(abs(t-5))

def attack_move(position):
    keyboard_controller = Keyboard()
    mouse_controller = Mouse()
    prev_pause = pyautogui.PAUSE
    pyautogui.PAUSE = 0.05

    pydirectinput.keyDown("x")
    pydirectinput.keyUp("x")
    pyautogui.moveTo(position)
    mouse_controller.press(Button.left)
    mouse_controller.release(Button.left)
    pyautogui.PAUSE = prev_pause

def do_jungle(pause=60, i_beep = True):
    frequency = 440
    duration = 300
    random.seed()

    def beep():
        if i_beep:
            winsound.Beep(frequency, duration)
            time.sleep(0.2)
            winsound.Beep(frequency, duration)
            time.sleep(1)

    tabbed_in = True
    while True:
        # pyautogui.PAUSE = 0.2
        beep()

        "Clears Gromp"
        tabbed_in = tab_into_league()
        original_pos = pyautogui.position()
        pyautogui.moveTo(camera_positions[camps["b_gromp"][0]])
        left_click()
        do_camp("b_gromp")
        pyautogui.moveTo(camera_positions[camps["b_blue"][0]])
        left_click()
        attack_move(camps["b_blue"][1])

        alt_tab(tabbed_in)
        # pyautogui.moveTo(original_pos)

        "Clears Blue"
        time.sleep(pause + random.uniform(-5, 10))
        beep()
        tabbed_in = tab_into_league()
        original_pos = pyautogui.position()

        pyautogui.moveTo(camera_positions[camps["b_blue"][0]])
        left_click()
        do_camp("b_blue")
        pyautogui.moveTo(camera_positions[camps["b_wolves"][0]])
        left_click()
        attack_move(camps["b_wolves"][1])

        alt_tab(tabbed_in)
        # pyautogui.moveTo(original_pos)

        "Clears Wolves"
        time.sleep(pause + random.uniform(-5, 10))
        beep()
        tabbed_in = tab_into_league()
        original_pos = pyautogui.position()

        do_camp("b_wolves")
        pyautogui.moveTo(camera_positions[camps["b_chickens"][0]])
        left_click()
        attack_move(camps["b_chickens"][1])

        alt_tab(tabbed_in)
        # pyautogui.moveTo(original_pos)

        "Clears chickens"
        time.sleep(pause + random.uniform(-5, 10))
        beep()
        tabbed_in = tab_into_league()
        original_pos = pyautogui.position()

        do_camp("b_chickens")
        pyautogui.moveTo(camera_positions[camps["b_chickens"][0]])
        left_click()
        pyautogui.moveTo(camera_positions[camps["b_red"][0]])
        left_click()
        attack_move(camps["b_red"][1])

        alt_tab(tabbed_in)
        # pyautogui.moveTo(original_pos)

        "Clears Red"
        time.sleep(pause + random.uniform(-5, 10))
        beep()
        tabbed_in = tab_into_league()
        original_pos = pyautogui.position()

        pyautogui.moveTo(camera_positions[camps["b_red"][0]])
        left_click()
        do_camp("b_red")
        pyautogui.moveTo(camera_positions[camps["b_krugs"][0]])
        left_click()
        attack_move(camps["b_krugs"][1])

        alt_tab(tabbed_in)
        # pyautogui.moveTo(original_pos)

        "Clears Krugs"
        time.sleep(pause + random.uniform(-5, 10))
        beep()
        tabbed_in = tab_into_league()
        original_pos = pyautogui.position()

        pyautogui.moveTo(camera_positions[camps["b_krugs"][0]])
        left_click()
        do_camp("b_krugs")
        pyautogui.moveTo(camera_positions[camps["b_gromp"][0]])
        left_click()
        attack_move(camps["b_gromp"][1])
        pyautogui.PAUSE = 0.5

        alt_tab(tabbed_in)
        # pyautogui.moveTo(original_pos)
        time.sleep(pause + random.uniform(-5, 10))
        # pyautogui.PAUSE = 0.5

def listen_tool(t=300):
    from pynput.mouse import Listener as mouse_listener
    from pynput.keyboard import Listener as key_listener


    def on_move(x, y):
        print("mouse is at position ({0}, {1})".format(x, y))

    def on_click(x, y, button, pressed):
        print("Pressed: {0} | Button: {1} | position ({2}, {3})".format(pressed, button, x, y))

    def on_scroll(x, y, dx, dy):
        print("Scrolling at ({0}, {1}) for dx: {2} and dy: {3}".format(x, y, dx, dy))

    def time_me(t):
        time.sleep(t)
        key_listener.stop()
        mouse_listener.stop()

    with mouse_listener(on_click=on_click, on_scroll=on_scroll) as ml:
        ml.join()
        time_me(t)

def goto_each():
    time.sleep(3)
    pyautogui.PAUSE = 3
    pyautogui.click(camera_positions[1])
    pyautogui.click(camps["b_gromp"][1], button="right")
    pyautogui.click(camps["b_blue"][1], button="right")
    pyautogui.click(camera_positions[camps["b_wolves"][0]], button="left")
    pyautogui.click(camps["b_wolves"][1], button="right")

    pyautogui.click(camera_positions[3])
    pyautogui.click(camps["b_chickens"][1], button="right")
    pyautogui.click(camps["b_red"][1], button="right")
    pyautogui.click(camera_positions[camps["b_krugs"][0]], button="left")
    pyautogui.click(camps["b_krugs"][1], button="right")
    pyautogui.mouseUp()
    pyautogui.PAUSE = 0.5

"""
[TESTING BEGINS]
"""
if __name__ == "__main__":

    # do_wolves()

    # listen_tool()

    # goto_each()

    do_jungle(60, i_beep = False)
    # do_camp("b_gromp")

    # tab_into_league()


    # time.sleep(2)

    # pyautogui.keyUp("alt")
    # pyautogui.click(button="right")


    # def main():
    #     do_wolves()
