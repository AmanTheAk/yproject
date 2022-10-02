import pyautogui #install this module using 'pip install PyAutoGUI'
import random

x = 0
y = 0

while True:
    user = pyautogui.confirm("choose option", buttons = ["rock", "paper", "scissor", "exit"])

    c = ["rock", "paper", "scissor"]
    random.shuffle(c)
    com = c[1]

    if user == com :
        pyautogui.alert(f"\t*****Tie*****\nyou chosse '{user, x}', computer choose '{com, y}'")

    elif user == "rock":
        if com == "scissor":
            x = x + 1
            pyautogui.alert(f"\t*****You Win*****\nyou chosse '{user, x}', computer choose '{com, y}'")
        else:
            y = y + 1
            pyautogui.alert(f"\t*****computer Win*****\nyou chosse '{user, x}', computer choose '{com, y}'")

    elif user == "paper":
        if com == "rock":
            x = x + 1
            pyautogui.alert(f"\t*****You Win*****\nyou chosse '{user, x}', computer choose '{com, y}'")
        else:
            y = y + 1
            pyautogui.alert(f"\t*****computer Win*****\nyou chosse '{user, x}', computer choose '{com, y}'")

    elif user == "scissor":
        if com == "paper":
            x = x + 1
            pyautogui.alert(f"\t*****You Win*****\nyou chosse '{user, x}', computer choose '{com, y}'")
        else:
            y = y + 1
            pyautogui.alert(f"\t*****computer Win*****\nyou chosse '{user, x}', computer choose '{com, y}'")

    elif user == "exit":
        break

if x > y:
    pyautogui.alert(f"\t*****You are Winner*****\nyour score '{x}', computer score '{y}'")
elif x == y :
    pyautogui.alert(f"\t*****Tie*****\nyour score '{x}', computer score '{y}'")
else :
    pyautogui.alert(f"\t*****Computer is Winner*****\nyour score '{x}', computer score '{y}'")
