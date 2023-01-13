"""
This script is moving your mouse in specific coordinates
If there are applications which can detect your presence based on the activity,
this little script will help you to stay online.
For sure the script can be improved.
"""


import sys
import pyautogui
import random
import time
from pynput import keyboard
import threading
# from pynput.mouse import Button, Controller


def move_mouse():
    """
    This function controls movement of the mouse.
    It receives x/y coordinates of the screen and duration which will be the time mouse needs to move from one location
    to another.
    It sleeps for 3 sec.
    """

    global cond
    
#     mouse = Controller()

    while cond:
        x = random.randint(300, 600)
        y = random.randint(200, 700)

        pyautogui.moveTo(x=x, y=y, duration=0.8)
        pyautogui.click(x=x, y=y)
#         mouse.press(Button.left)
#         mouse.release(Button.left)
        time.sleep(3)


def key_pressed(key):
    """
    Listening for a pressed key and based on that it will stop this function.
    With this function we change the global cond and with that it will stop mouse movement function
    @param key: key received from the keyboard
    """

    global cond

    # we choose esc key from the keyboard
    if key == keyboard.Key.esc:
        cond = False
        sys.exit()


cond = True

# creating a Listener
keyboard_list = keyboard.Listener(on_release=key_pressed)

# implementing Thread in order to run simultaneously the above both function
event = threading.Thread(target=move_mouse)
event.start()

# it could be that we can run Lister in another way, but this was my first try
# Listener is invoked with context manager
with keyboard_list:
    while cond:
        keyboard_list.join()  # it could be used maybe with another function

