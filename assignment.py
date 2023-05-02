import pyautogui
import threading
import time

inp = input("press enter to start")
pyautogui.moveTo(510,882,1)
pyautogui.click()
awesome = True
def autoclick():
    pyautogui.moveTo(1000,484)
    tally = 0
    while awesome:
        pyautogui.click()
        tally = tally + 1
        if tally == 100:
            levelup()

def levelup():
    level = pyautogui.locateOnScreen('assets/Level Up.png',confidence=0.9)
    if level == None:
        newhire()
    else:
        pyautogui.moveTo(level)
        pyautogui.click()
        levelup()
def newhire():
    level = pyautogui.locateOnScreen('assets/Hire.png',confidence=0.8)
    if level == None:
        nextlevel()
    else:
        pyautogui.moveTo(level)
        pyautogui.click()
        newhire()
def nextlevel():
    stage = pyautogui.locateOnScreen('assets/New Stage.png',confidence=0.6)
    if stage == None:
        timer()
    else:
        pyautogui.moveTo(stage)
        pyautogui.click()
        nextlevel()
def timer():
    clock = pyautogui.locateOnScreen('assets/Timer.png',confidence=0.8)
    if clock == None:
        autoclick()
    else:
        pyautogui.moveTo(942,190)
        pyautogui.click()
        nextlevel()
autoclick()