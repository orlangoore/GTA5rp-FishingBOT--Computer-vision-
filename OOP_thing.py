
import cv2
from mss.linux import MSS as mss
import time
import pyautogui
import mss
import numpy
import pyautogui
import random
import os
import sys
import keyboard as kb
import random
import pynput
from pynput.mouse import Controller
from pynput import keyboard
from tkinter import *
from playsound import playsound



class FishingBot():
    def __init__(self):
        self.bobber_pic = "img\\poplavok2.png"
        self.keyboardd = keyboard.Controller()
        self.mouse = Controller()
        self.monitor_width, self.monitor_height = pyautogui.size()
        self.counter1 = 0



    # def process_image(self, original_image):
    #     processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    #
    #     processed_image = cv2.Canny(processed_image, threshold1=200, threshold2=300)
    #     return processed_image



    def mouse_starting_position(self):
        self.mouse.position = (random.uniform(int(self.monitor_width / 3 + 600), int(self.monitor_width / 2 + 600)),
                               random.uniform(int(self.monitor_height / 3), int(self.monitor_height / 2)))



    def klick(self):
        pyautogui.moveTo(random.uniform(int(self.monitor_width / 3 + 600), int(self.monitor_width / 2 + 600)),
                               random.uniform(int(self.monitor_height / 3), int(self.monitor_height / 2)))
        self.mouse.click(pynput.mouse.Button.left, 1)

    def click_the_rod(self):
        try:
            x, y = pyautogui.locateCenterOnScreen("C:\\new\\img\\mk5.jpg", confidence=.9)
        except:
            pass
        try:
            pyautogui.moveTo(x, y)
            pyautogui.click()
        except:
            self.click_the_rod()

    def click_the_menu(self):
        try:
            x, y = pyautogui.locateCenterOnScreen("C:\\new\\img\\primanka.jpg", confidence=.9)
        except:
            pass
        try:
            pyautogui.moveTo(x, y)
            pyautogui.click()
        except:
            self.click_the_menu()


    def zakinut(self):
        self.mouse_starting_position()
        self.mouse.click(pynput.mouse.Button.left, random.randint(1, 2))
        time.sleep(random.uniform(0.1, 0.3))
        self.keyboardd.press("i")
        time.sleep(random.uniform(0.06, 0.15))
        self.keyboardd.release("i")
        time.sleep(random.uniform(0.4, 0.5))
        self.click_the_rod()
        time.sleep(random.uniform(1, 3))
        self.click_the_menu()
        time.sleep(random.uniform(0.2, 0.3))




    def zakinutt(self):
        if kb.is_pressed('e') == True:
            self.zakinut()


    def stop(self):
        if kb.is_pressed('m') == True:
            print('Nazhal Knopku')
            sys.exit()


    def ss_more(self):
        while True:
            op = 1
            vremja = 1
            with mss.mss() as sct:
                monitor = {"top": 0, "left": 0, "width": self.monitor_width + 100, "height": self.monitor_height + 100}
                while "Screen capturing":
                    if kb.is_pressed('m') == True:
                        sys.exit()
                    elif kb.is_pressed('e') == True:
                        self.zakinut()
                    else:
                        img = numpy.array(sct.grab(monitor))
                        template = cv2.imread(self.bobber_pic, cv2.IMREAD_GRAYSCALE)
                        w, h = template.shape[::-1]
                        gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        res = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)
                        threshold = .8
                        loc = numpy.where(res >= threshold)
                        op += 1
                        self.zakinutt()
                        print(op)
                        for pt in zip(*loc[::-1]):
                            cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
                            barada = cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
                            self.counter1  = 0
                            self.counter1  = len(barada)
                    while self.counter1  != 0:
                        vremja = op
                        self.counter1  = 0
                        self.klick()
                    if op - vremja > 10 and op - vremja < 12:
                        self.zakinut()
                        self.counter1  = 0



boteg = FishingBot()

boteg.ss_more()










