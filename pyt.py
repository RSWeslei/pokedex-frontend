

import pyautogui as pg
import time

# 544 Y:  450 RGB: (157, 160, 170)
inicialPos = (544+90, 450)
# wait 2 seconds
time.sleep(2)

# mouse position
# pg.displayMousePosition()
# for 18 times
for i in range(18):
    # move to the initial position
    pg.moveTo(inicialPos)
    # click
    # move to the next position
    inicialPos = inicialPos[0] + 90, inicialPos[1]
    # if i == 9 down 20px the mouse
    if i == 9:
        inicialPos = inicialPos[0], inicialPos[1] + 20
    pg.click()
    pg.click()
    time.sleep(0.2)
    # X: 1840 Y:  238 RGB: ( 44,  44,  44)
    pg.moveTo(1840, 238)
    pg.click()
    time.sleep(0.2)
    #X: 1849 Y:  288 RGB: ( 12, 140, 233)
    pg.moveTo(1849, 288)
    pg.click()
    time.sleep(0.2)
    #X: 1796 Y:  280 RGB: ( 44,  44,  44)
    pg.moveTo(1796, 280)
    pg.click()
    time.sleep(0.2)
    # wait 1 second
    time.sleep(1)