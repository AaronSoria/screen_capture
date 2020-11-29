import numpy as np
import cv2
import pyautogui
import datetime
import time
import os

while True:
	image = pyautogui.screenshot()
	image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
	ct = datetime.datetime.now()
	name =  os.getcwd() + "/screenshot_" + str(ct) + ".png"
	cv2.imwrite(name, image) 
	time.sleep(1)
