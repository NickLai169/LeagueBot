import pyautogui
import pydirectinput
import time
import os
import sys
from functions import *
import winsound
import ctypes

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
    4: (1800, 1038),
    }

camps = {
    "b_gromp": [1, (334, 503)],
    "b_blue": [1, (1466, 802)],
    "b_wolves": [2, (1183, 886)],
    "b_chickens": [3, (683, 95)],
    "b_red": [3, (1322, 806)],
    "b_krugs": [4, (963, 89)],
    }

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
        tab_into_league()

        time.sleep(0.5)
        pyautogui.PAUSE = 0.25
        original_pos = pyautogui.position()
        pyautogui.click(x=1714, y=948, button='left')
        pyautogui.moveTo(1183, 886)
        pyautogui.click(x=1183, y=886, button='right')

        pyautogui.PAUSE = 0.05
        alt_tab()

        pyautogui.moveTo(original_pos)
        pyautogui.PAUSE = 0.5
        time.sleep(abs(t-5))

def attack_move(position):
    prev_pause = pydirectinput.PAUSE
    pydirectinput.PAUSE = 0.1
    print(position)
    pydirectinput.keyDown("x")
    pydirectinput.keyUp("x")
    print("pressed x")

    pyautogui.mouseDown(position, button="left")
    pyautogui.mouseUp(position, button="left")

    pydirectinput.PAUSE = prev_pause

def do_camps():
    frequency = 440
    duration = 300
    while True:
        winsound.Beep(frequency, duration)
        time.sleep(0.2)
        winsound.Beep(frequency, duration)

        "Clears Gromp"
        tab_into_league()
        original_pos = pyautogui.position()
        pyautogui.click(camera_positions[1])
        pyautogui.click(camps["b_gromp"][1], button="right")
        attack_move(camps["b_blue"][1])

        alt_tab()
        pyautogui.moveTo(original_pos)

        "Clears Blue"
        time.sleep(60)
        winsound.Beep(frequency, duration)
        time.sleep(0.2)
        winsound.Beep(frequency, duration)
        time.sleep(1)
        tab_into_league()
        original_pos = pyautogui.position()

        pyautogui.click(camps["b_blue"][1], button="right")
        pyautogui.click(camera_positions[camps["b_wolves"][0]], button="left")
        attack_move(camps["b_wolves"][1])

        alt_tab()
        pyautogui.moveTo(original_pos)

        "Clears Wolves"
        time.sleep(60)
        winsound.Beep(frequency, duration)
        time.sleep(0.2)
        winsound.Beep(frequency, duration)
        time.sleep(1)
        tab_into_league()
        original_pos = pyautogui.position()

        pyautogui.click(camps["b_wolves"][1], button="right")
        pyautogui.click(camera_positions[3])

        attack_move(camps["b_chickens"][1])

        alt_tab()
        pyautogui.moveTo(original_pos)

        "Clears chickens"
        time.sleep(60)
        winsound.Beep(frequency, duration)
        time.sleep(0.2)
        winsound.Beep(frequency, duration)
        time.sleep(1)
        tab_into_league()
        original_pos = pyautogui.position()

        pyautogui.click(camps["b_chickens"][1], button="right")
        attack_move(camps["b_red"][1])

        alt_tab()
        pyautogui.moveTo(original_pos)

        "Clears Red"
        time.sleep(60)
        winsound.Beep(frequency, duration)
        time.sleep(0.2)
        winsound.Beep(frequency, duration)
        time.sleep(1)
        tab_into_league()
        original_pos = pyautogui.position()

        pyautogui.click(camps["b_red"][1], button="right")
        pyautogui.click(camera_positions[camps["b_krugs"][0]], button="left")

        attack_move(camps["b_krugs"][1])

        alt_tab()
        pyautogui.moveTo(original_pos)

        "Clears Krugs"
        time.sleep(60)
        winsound.Beep(frequency, duration)
        time.sleep(0.2)
        winsound.Beep(frequency, duration)
        time.sleep(1)
        tab_into_league()
        original_pos = pyautogui.position()

        pyautogui.click(camps["b_krugs"][1], button="right")
        pyautogui.click(camera_positions[camps["b_gromp"][0]], button="left")
        attack_move(camps["b_gromp"][1])
        pyautogui.PAUSE = 0.5

        time.sleep(60)


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

# do_wolves()

# listen_tool()

# goto_each()

# do_camps()

time.sleep(2)

attack_move(pyautogui.position())




# time.sleep(2)

# pyautogui.keyUp("alt")
# pyautogui.click(button="right")


# def main():
#     do_wolves()
# if __name__ == "__main__":
#     main()
