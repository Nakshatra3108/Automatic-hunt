import keyboard
import pyautogui

def on_keypress(event):
    if event.name == 'f5':
        x, y = pyautogui.position()
        print(f"Mouse coordinates: ({x}, {y})")

keyboard.on_press(on_keypress)
keyboard.wait('esc')