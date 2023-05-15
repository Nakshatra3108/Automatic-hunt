import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import webbrowser
import pyautogui
import keyboard


pth="C:\\Users\\Lenovo\\Downloads"

def cipher_identifier():
    url = "https://www.dcode.fr/cipher-identifier"
    webbrowser.open(url)
def backlink_identifier():
    url = "https://blidentifier.netlify.app/"
    webbrowser.open(url)

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        nm,ext=os.path.splitext(event.src_path)
        time.sleep(1)
        
        if ext in ['.jpg', '.jpeg', '.png', '.gif', '.jfif']:
            url = 'https://aperisolve.fr/'
            webbrowser.open(url)
            time.sleep(2)
            #Select File Button
            pyautogui.click(947, 613, 1)
            time.sleep(1)
            pyautogui.write(event.src_path)
            pyautogui.press('enter')
            time.sleep(3)

            url2='https://stylesuxx.github.io/steganography/'
            webbrowser.open(url2)
            time.sleep(1)
            #Decode button next to encode
            pyautogui.click(503, 209, 1)
            time.sleep(0.5)
            #Choose file button
            pyautogui.click(444, 429, 1)
            time.sleep(1)
            pyautogui.write(event.src_path)
            pyautogui.press('enter')
            time.sleep(1)
            #Decode button
            pyautogui.click(1504, 475, 1)



keyboard.add_hotkey("F5", cipher_identifier)
keyboard.add_hotkey("F6", backlink_identifier)

event_handler=FileMovementHandler()
observer=Observer()
observer.schedule(event_handler, pth, recursive=True)
observer.start()
try:
    while True:
        for i in range(4):
            print('Running' + '.' * i, end='\r', flush=True)
            time.sleep(0.5)
        print('Running    ', end='\r', flush=True)
except KeyboardInterrupt:
    print('Stopped')
    observer.stop()