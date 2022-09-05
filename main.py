
import pyautogui as gui
import time
import os
import keyboard
import multiprocessing
import tkinter as tk




def d_handler():
    while(keyboard.is_pressed('q') == False):
        
        while gui.pixelMatchesColor(1050, 1250, (250, 250, 0), tolerance=20):
            gui.keyDown("d")
            
            if gui.pixelMatchesColor(1050, 1250, (250, 250, 0), tolerance=20) == False:
                gui.keyUp("d")
                break        

def f_handler():
     while(keyboard.is_pressed('q') == False):
        
        while gui.pixelMatchesColor(1200, 1250, (250, 250, 0), tolerance=20):
            gui.keyDown("f")
            
            if gui.pixelMatchesColor(1200, 1250, (250, 250, 0), tolerance=20) == False:
                gui.keyUp("f")
                break

def j_handler():
     while(keyboard.is_pressed('q') == False):
        
        while gui.pixelMatchesColor(1350, 1250, (250, 250, 0), tolerance=20):
            gui.keyDown("j")
            
            if gui.pixelMatchesColor(1350, 1250, (250, 250, 0), tolerance=20) == False:
                gui.keyUp("j")
                break
            


def k_handler():
     while(keyboard.is_pressed('q') == False):
        
        while gui.pixelMatchesColor(1500, 1250, (250, 250, 0), tolerance=20):
            gui.keyDown("k")
            
            if gui.pixelMatchesColor(1500, 1250, (250, 250, 0), tolerance=20) == False:
                gui.keyUp("k")
                break
        

def miss_handler():
    global misses 
    misses = 0
    
    while(keyboard.is_pressed('q') == False):
            
            
        if gui.pixelMatchesColor(1050, 1350, (250, 0, 0), tolerance=20) == False:
            misses += 1
            break

        if gui.pixelMatchesColor(1200, 1350, (250, 0, 0), tolerance=20) == False:
            misses += 1
            break

        if gui.pixelMatchesColor(1350, 1350, (250, 0, 0), tolerance=20) == False:
            misses += 1
            break

        if gui.pixelMatchesColor(1500, 1350, (250, 0, 0), tolerance=20) == False:
            misses += 1
            break



d_process = multiprocessing.Process(target=d_handler)
f_process = multiprocessing.Process(target=f_handler)
j_process = multiprocessing.Process(target=j_handler)
k_process = multiprocessing.Process(target=k_handler)
miss_process = multiprocessing.Process(target=miss_handler)

def start():
    d_process.start()
    f_process.start()
    j_process.start()
    k_process.start()
    miss_process.start()








if __name__ == "__main__":
    win = tk.Tk()
    win.title('Guitar Zero')
    win.geometry('200x100')
    start_button = tk.Button(win, text='Start', command=start, )
    start_button.pack(side='right', fill='none', expand=True, padx= 10, pady= 10)
    
    frame = tk.Frame(win, relief='groove', borderwidth=2, width= 70 , height= 50)
    frame.pack(side='left',fill='x', expand=True, padx= 10, pady= 10)
    counter = tk.Label(frame, text='Misses: ')
    counter.pack(side='left')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    win.mainloop()


    

    
    
    
    








