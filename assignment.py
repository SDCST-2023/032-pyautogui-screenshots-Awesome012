import pyautogui
import os

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
            upgrades()

def levelup():
    level = pyautogui.locateOnScreen('assets/Level Up.png',confidence=0.85)
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
    pyautogui.moveTo(1058,193)
    pyautogui.click()
    timer()

def timer():
    clock = pyautogui.locateOnScreen('assets/Timer.png',confidence=0.8)
    if clock == None:
        autoclick()
    else:
        pyautogui.moveTo(942,190)
        pyautogui.click()
        timer()
def upgrades():
    directory = os.listdir('Icons/')
    for file in directory:
        check = pyautogui.locateOnScreen(f'Icons/{file}',confidence=0.7)
        print(check)
        if check == None:
            levelup()
        else:
            pyautogui.moveTo(check)
            pyautogui.click()
            pyautogui.moveTo(1000,400,0.1)

autoclick()
