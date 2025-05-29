import sys
print(f"Python executable being used: {sys.executable}")
print(f"Python version being used: {sys.version}")

import pyautogui
import time
import keyboard

counter = 0
sleepTime = 1

print("Starting...")
print("Hold ESC to exit")

while True:
    if keyboard.is_pressed('esc'):
        break
    try:
        button = pyautogui.locateOnScreen('button.png')
        if button:
            pyautogui.click(button.left + button.width // 2, button.top + button.height // 2)
            counter += 1
            print(f"Button clicked ({counter} times)")
            time.sleep(sleepTime)

    except pyautogui.ImageNotFoundException:
        print(f"Button not found. Trying again in {sleepTime} seconds...")
        pyautogui.moveTo(960, 540)

print("Exiting...")