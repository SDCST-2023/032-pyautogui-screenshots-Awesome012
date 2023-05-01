import pyautogui
import threading
import time

inp = input("press enter to start")
pyautogui.moveTo(510,882,1)
pyautogui.click()
awesome = True
def autoclick():
    while awesome:
        pyautogui.moveTo(1000,484)
        pyautogui.click()
def levelup():
    level = pyautogui.locateOnScreen('assets/Level Up.png',confidence=0.7)
    if level == None:
        autoclick()
    else:
        pyautogui.moveTo(level)
        pyautogui.click()
        levelup()

autoclick()