from tkinter import *
from tkinter import ttk
# import keyboard
import pyautogui

# global variables
width, height = pyautogui.size()  # screen size
colorPos = purplePos = commentPos = savePos = locationPos = 0


# Create an instance of tkinter frame or window
win = Tk()
# Set the geometry of tkinter frame
win.geometry("400x400")  # main window
win.title("Main Window")
ttk.Label(win, text="Welcome!", font=("Helvetica", 25)
          ).pack(padx=15, pady=5, ipadx=15, ipady=15)


def open_win():  # opens new window for the tutorial
    new = Toplevel(win)
    new.geometry("600x600")
    new.title("Set Up Tutorial")
    # Create a Label in New window

    # frames created below
    topframe = Frame(new)
    topframe.pack()
    midframe = Frame(new)
    midframe.pack()
    botframe = Frame(new)
    botframe.pack(side=BOTTOM, pady=20)
    
    # start of topframe
    # step 1:
    Label(topframe, text="STEP 1: Hover over the color button and press 1").pack()

    # step 2:
    Label(topframe, text="STEP 2: Hover over the purple and press 2",font=("Helvetica", 20)).pack()

    # step 3: 
    Label(topframe, text="STEP 3: Hover over the comment attribute box and press 3").pack()
    # step 4: 
    Label(topframe, text="STEP 4: Hover over the save measurment button and press 4").pack()
    # step 5:
    Label(topframe, text="STEP 5: Hover over the location button and press 5").pack()

    # buttom frame begins
    ttk.Button(botframe, text='Close', command=new.destroy).pack(padx=10,pady=10,ipadx=20,ipady=60)
    # buttom frame ends
    new.grab_set()

# Create a label
Label(win, text="Click the below button to start set up",
      font=('Helvetica 17 bold')).pack(pady=30)
# Create a button to open a New Windows
ttk.Button(win, text='Set Up Tutortial', command=open_win).pack()
ttk.Button(win, text='Close', command=win.destroy).pack(
    padx=10, pady=10, ipadx=20, ipady=60)
win.mainloop()
