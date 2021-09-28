from os import name
from tkinter import *
from tkinter import ttk
# import keyboard
import pyautogui

# global variables
width, height = pyautogui.size()  # screen size
colorPos = purplePos = commentPos = savePos = locationPos = 0


# Create an instance of tkinter frame or window
win = Tk()
# set up tkinter global variables
colorVar = StringVar(); colorVar.set(colorVar)
purpleVar = StringVar(); purpleVar.set(purplePos)
commentVar = StringVar(); commentVar.set(commentPos)
saveVar = StringVar(); saveVar.set(savePos)
locationVar = StringVar(); locationVar.set(locationPos)
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
    Label(topframe, text="STEP 2: Hover over the purple and press 2",
          font=("Helvetica", 20)).pack()

    # step 3:
    Label(topframe, text="STEP 3: Hover over the comment attribute box and press 3").pack()
    # step 4:
    Label(topframe, text="STEP 4: Hover over the save measurment button and press 4").pack()
    # step 5:
    Label(topframe, text="STEP 5: Hover over the location button and press 5").pack()

    # end of steps/ status 
    test = Label(topframe, text="current action: ", font=(
        "Helvetica", 25), borderwidth=1, relief="solid", bg="white", fg="black")#needs fixing
    new.bind('1', step1)
    new.bind('2', step2)
    new.bind('3', step3)
    new.bind('4', step4)
    new.bind('5', step5)
    test.pack(padx=15, pady=15, ipadx=15, ipady=15)
    # end of top frame stuff

    # midframe begins
    Label(midframe, text="Current X and Y Positions Seperated by a Space").pack()
    f1 = Frame(midframe); f1.pack()
    f2 = Frame(midframe); f2.pack()
    f3 = Frame(midframe); f3.pack()
    f4 = Frame(midframe); f4.pack()
    f5 = Frame(midframe); f5.pack()
    Label(f1, text="Position of Color Button: ").pack(side=LEFT)
    Label(f1, textvariable=colorVar).pack(side=LEFT)
    Label(f2, text="Position of Purple Color: ").pack(side=LEFT)
    Label(f2, textvariable=purpleVar).pack(side=LEFT)
    Label(f3, text="Position of Comment Section: ").pack(side=LEFT)
    Label(f3, textvariable=commentVar).pack(side=LEFT)
    Label(f4, text="Position of Save Button: ").pack(side=LEFT)
    Label(f4, textvariable=saveVar).pack(side=LEFT)
    Label(f5, text="Position of Location Button: ").pack(side=LEFT)
    Label(f5, textvariable=locationVar).pack(side=LEFT)
    # lab1 = Label(midframe, text=colorText, font=('helvetica',12,'bold')).pack()
    # midframe ends

    # buttom frame begins
    ttk.Button(botframe, text='Close', command=new.destroy).pack(
        padx=10, pady=10, ipadx=20, ipady=60)
    # buttom frame ends
    new.grab_set()

#############  helper methods: ###################
def step1(event):  # works fine
    global colorPos
    colorPos = pyautogui.position()
    colorVar.set(colorPos)#update global pos

def step2(event): #works fine
    global purplePos
    purplePos = pyautogui.position()
    purpleVar.set(purplePos)#update global pos

def step3(event): #works fine
    global commentPos
    commentPos = pyautogui.position()
    commentVar.set(commentPos)#update global pos

def step4(event): #works fine
    global savePos
    savePos = pyautogui.position()
    saveVar.set(savePos)#update global pos

def step5(event): #works fine
    global locationPos
    locationPos = pyautogui.position()
    locationVar.set(locationPos)#update global pos

def tempDisplay(): # need to make this work with display 
    print("color postion: ", colorPos)
    print("purple postion: ", purplePos)
    print("comment postion: ", commentPos)
    print("save postion: ", savePos)
    print("location button: ", locationPos)

############# End of Helpers ##################

tempDisplay()
# Create a label
Label(win, text="Click the below button to start set up",
      font=('Helvetica 17 bold')).pack(pady=30)
# Create a button to open a New Windows
ttk.Button(win, text='Set Up Tutortial', command=open_win).pack()
ttk.Button(win, text='Close', command=win.destroy).pack(
    padx=10, pady=10, ipadx=20, ipady=60)
win.mainloop()

tempDisplay()
