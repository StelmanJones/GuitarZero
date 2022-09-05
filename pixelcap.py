import pyautogui as gui
import time
import os



class PixelCap:

    d_trigger = 0
    f_trigger = 0
    j_trigger= 0
    k_trigger = 0


    def __init__(self):
        self.d_trigger = gui.pixelMatchesColor(1050, 1250, (250, 250, 0), tolerance=20)
        self.f_trigger = gui.pixelMatchesColor(1200, 1250, (250, 250, 0), tolerance=20)
        self.j_trigger = gui.pixelMatchesColor(1350, 1250, (250, 250, 0), tolerance=20)
        self.k_trigger = gui.pixelMatchesColor(1500, 1250, (250, 250, 0), tolerance=20)

    
    def get_pixels(self):
        (print("PixelCap process started"))
        while(True):
            self.d_trigger = gui.pixelMatchesColor(1050, 1250, (250, 250, 0), tolerance=20)
            self.f_trigger = gui.pixelMatchesColor(1200, 1250, (250, 250, 0), tolerance=20)
            self.j_trigger = gui.pixelMatchesColor(1350, 1250, (250, 250, 0), tolerance=20)
            self.k_trigger = gui.pixelMatchesColor(1500, 1250, (250, 250, 0), tolerance=20)

            #print(f'D: {self.d_value} F: {self.f_value} J: {self.j_value} K: {self.k_value}')
            