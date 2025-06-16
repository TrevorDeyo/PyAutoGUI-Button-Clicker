---

# PyAutoGUI Button Clicker

This script automates clicking a specific button on your screen using the `pyautogui` library. It continuously searches for an image of the button and clicks it when found.

---

## Features

* **Automated Clicking:** Finds and clicks a target button on the screen.
* **Counter:** Keeps track of how many times the button has been clicked.
* **User-Friendly Exit:** Easily stop the script by holding the `ESC` key.

---

## Requirements

Before running the script, you'll need to install the necessary Python libraries:

* `pyautogui`
* `keyboard`

You can install them using pip:

```bash
pip install pyautogui keyboard
```

---

## How to Use

1.  **Prepare your button image:**
    Save an image of the button you want to click as `button.png` in the same directory as the script. Make sure the image is clear and represents only the button you want to interact with.

2.  **Run the script:**
    Execute the script from your terminal:

    ```bash
    python your_script_name.py
    ```
    (Replace `your_script_name.py` with the actual name of your Python file.)

3.  **Monitor the script:**
    The script will start searching for and clicking the button. You'll see messages in your console indicating its progress.

4.  **Exit the script:**
    To stop the script at any time, simply **hold down the `ESC` key**.

---

## Script Logic

The script works as follows:

* It initializes a `counter` to track clicks and sets a `sleepTime` for delays between actions.
* It enters an infinite loop that constantly checks for the `ESC` key press to exit.
* Inside the loop, it uses `pyautogui.locateOnScreen('button.png')` to find the location of the `button.png` image on the screen.
* If the button is found, it calculates the center of the button and uses `pyautogui.click()` to click it. The `counter` is then incremented.
* If `button.png` is not found, a message is printed, and the mouse cursor is moved to the center of the screen (960, 540) to prevent it from getting stuck in an invisible loop if the button moves or disappears.
* A `time.sleep()` is used to pause the script for `sleepTime` seconds after each click or failed attempt, preventing it from consuming too many resources.

---
