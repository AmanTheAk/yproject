import pyautogui
import webbrowser
import time

mob = input("Enter target mobile number with country code : ")
message = input("Enter a message : ")
no = int(input("Enter the number of message you want to send : "))
interval = int(input("Give a interval between each message : "))

webbrowser.open_new_tab(f"https://web.whatsapp.com/send?phone={mob}&text={message}")
time.sleep(15 + interval)
pyautogui.hotkey('enter')
time.sleep(interval)

for i in range(no-1):
    pyautogui.typewrite(f"{message}")
    time.sleep(interval)
    pyautogui.hotkey('enter')
    time.sleep(interval)
