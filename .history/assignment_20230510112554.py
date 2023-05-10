import pyautogui
import os
import threading
import time

inp = input("press enter to start")
pyautogui.moveTo('assets/Unititled.png')
pyautogui.click()
awesome = True

def play1():
    while awesome:
        button = pyautogui.locateOnScreen('assets/PLay Now.png',confidence=0.85)


def autoclick():
    pyautogui.moveTo(1000,484)
    while awesome:
        pyautogui.click()

def levelup():
    while awesome:
        level = pyautogui.locateOnScreen('assets/Level Up.png',confidence=0.85)
        if level == None:
            None
        else:
            pyautogui.moveTo(level)
            pyautogui.click()

def levelup2():
    while awesome:
        level2 = pyautogui.locateOnScreen('assets/Level Up 2.png',confidence=0.85)
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
            None
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


Thread(target = play1).start()
Thread(target = play2).start()
Thread(target = play3).start()
Thread(target = movebar).start()