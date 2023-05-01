import pyautogui
import threading
import time

inp = input("press enter to start")
pyautogui.moveTo(510,882,1)
pyautogui.click()
awesome = True
def autoclick():
    tally = 0
    while awesome:
        pyautogui.moveTo(1000,484)
        pyautogui.click()
        tally = tally + 1
        levelup()
def levelup():
    level = pyautogui.locateOnScreen('assets/Level Up.png',confidence=0.9)
    if level == None:
        autoclick()
    else:
        pyautogui.moveTo(level)
        pyautogui.click()
        levelup()
def nextlevel():
    level = pyautogui.locateOnScreen('assets/Level Up.png',confidence=0.9)

autoclick()