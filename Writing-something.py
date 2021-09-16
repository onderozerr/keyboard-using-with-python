#this can be a message bot 

import pyautogui
import time

t = input("input the message:")
r = int(input("input number of message:"))
# 5 seconds for you to click the chat
time.sleep(5)


for n in range(r):
    pyautogui.write(t)
    pyautogui.hotkey('enter')
