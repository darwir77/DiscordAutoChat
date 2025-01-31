import pyautogui
import time
import random

pyautogui.PAUSE = 1

#place your list of text here
Message = []

Time1 = [65, 66, 67, 68, 69]
Time2 = [310, 311, 312, 313, 314]

# Start Program 

print(len(Message))

time.sleep(2)

while True:
    randomNumberForMessage = random.randint(0, len(Message)-1)
    randomNumberForTimeCooldown = random.randint(0, len(Time1)-1)

    #place your x & y coordinate here
    pyautogui.moveTo(371, 857)
    
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.write(Message[randomNumberForMessage])
    time.sleep(0.5)
    pyautogui.click()
    pyautogui.press('enter')

    time.sleep(Time1[randomNumberForTimeCooldown])