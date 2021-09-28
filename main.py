from tkinter import *
from tkinter import ttk
#import keyboard
import pyautogui

#global variables
width, height = pyautogui.size()  # screen size
colorPos = purplePos = commentPos = savePos = locationPos = 0


# Create an instance of tkinter frame or window
win = Tk()
# Set the geometry of tkinter frame
win.geometry("400x400")  # main window
win.title("Main Window")
ttk.Label(win, text="Welcome!", font=("Helvetica", 25)
          ).pack(padx=15, pady=5, ipadx=15, ipady=15)


def open_win(): #opens new window for the tutorial
    new = Toplevel(win)
    new.geometry("600x600")
    new.title("Set Up Tutorial")
    # Create a Label in New window
    
    #frames created below
    topframe = Frame(new)
    topframe.pack()
    midframe = Frame(new)
    midframe.pack()
    botframe = Frame(new)
    botframe.pack(side=BOTTOM, pady=20)

    #buttom frame begins
    ttk.Button(botframe, text='Close', command=new.destroy).pack(padx=10,pady=10,ipadx=20,ipady=60)
    #buttom frame ends
    new.grab_set()

# Create a label
Label(win, text="Click the below button to start set up",
      font=('Helvetica 17 bold')).pack(pady=30)
# Create a button to open a New Windows
ttk.Button(win, text='Set Up Tutortial', command=open_win).pack()
ttk.Button(win, text='Close', command=win.destroy).pack(
    padx=10, pady=10, ipadx=20, ipady=60)
win.mainloop()
