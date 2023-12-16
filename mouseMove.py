import pyautogui as pag
import time
import random

if __name__ == '__main__':
    while True:
        x = random.randint(600, 700)
        y = random.randint(200, 500)
        pag.moveTo(x, y, 0.5)
        time.sleep(2)
exit()

