import pyautogui
import os
from threading import Thread
import time

inp = input("press enter to start")
pyautogui.moveTo('assets/FireFox.png')
pyautogui.click()
awesome = True

def play1():
    while awesome:
        button = pyautogui.locateOnScreen('assets/Play Now.png',confidence=0.85)
        if button == None:
            None
        else:
            pyautogui.moveTo(button)
            pyautogui.click()

def play2():
    while awesome:
        button = pyautogui.locateOnScreen('assets/Green Play.png',confidence=0.85)
        if button == None:
            None
        else:
            pyautogui.moveTo(button)
            pyautogui.click()

def play3():
    while awesome:
        button = pyautogui.locateOnScreen('assets/Exit.png',confidence=0.85)
        if button == None:
            None
        else:
            pyautogui.moveTo(button)
            pyautogui.click()

def autoclick():
    pyautogui.moveTo(1000,484)
    while awesome:
        pyautogui.click()

def levelup():
    while awesome:
        level = pyautogui.locateOnScreen('assets/Level Up.png',confidence=0.9)
        if level == None:
            None
        else:
            pyautogui.moveTo(level)
            pyautogui.click()

def levelup2():
    while awesome:
        level2 = pyautogui.locateOnScreen('assets/Level Up 2.png',confidence=0.9)
        if level2 == None:
            None
        else:
            pyautogui.moveTo(level2)
            pyautogui.click()

def newhire():
    while awesome:
        level3 = pyautogui.locateOnScreen('assets/Hire.png',confidence=0.85)
        if level3 == None:
            None
        else:
            pyautogui.moveTo(level3)
            pyautogui.click()

def nextlevel():
    while awesome:
        time.sleep(30)
        pyautogui.moveTo(1058,193)
        pyautogui.click()

def timer():
    while awesome:
        clock = pyautogui.locateOnScreen('assets/Timer.png',confidence=0.8)
        if clock == None:
            pyautogui.moveTo(1000,484)
            pyautogui.click()
        else:
            pyautogui.moveTo(942,190)
            pyautogui.click()

def upgrades():
    while awesome:
        directory = os.listdir('Icons/')
        for file in directory:
            check = pyautogui.locateOnScreen(f'Icons/{file}',confidence=0.7)
            if check == None:
                None
            else:
                pyautogui.moveTo(check)
                pyautogui.click()
                pyautogui.moveTo(1000,400)

if __name__ == "__main__": 
    Thread(target = play1).start()
    Thread(target = play2).start()
    Thread(target = play3).start()
    Thread(target = timer).start()
    Thread(target = autoclick).start()
    Thread(target = upgrades).start()
    Thread(target = levelup).start()
    Thread(target = levelup2).start()
    Thread(target = newhire).start()
    Thread(target = nextlevel).start()
