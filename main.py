#Credits:
#Original code by: Nixon Lazaro
#Modified by: Ifte Ahmed
#DOT SDG SCRIPT

from tkinter import *
from tkinter import ttk
import keyboard
import pyautogui
import pickle
import time

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
win.geometry("500x500")  # main window
win.title("Main Window")
ttk.Label(win, text="Welcome!", font=("Helvetica", 25)
          ).pack(padx=15, pady=15)


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
    Label(topframe, text="STEP 1: Hover over the color button and press 1",
          font=("Helvetica", 20)).pack()
    # step 2:
    Label(topframe, text="STEP 2: Hover over the purple and press 2",
          font=("Helvetica", 20)).pack()
    # step 3:
    Label(topframe, text="STEP 3: Hover over the comment attribute box and press 3",
          font=("Helvetica", 20)).pack()
    # step 4:
    Label(topframe, text="STEP 4: Hover over the save measurment button and press 4",
          font=("Helvetica", 20)).pack()
    # step 5:
    Label(topframe, text="STEP 5: Hover over the location button and press 5",
          font=("Helvetica", 20)).pack()

    # end of steps/ status 
    test = Label(topframe, text="Current Location Values Below: ", font=(
        "Helvetica", 15), borderwidth=1, relief="solid", bg="white", fg="black")#needs fixing
    new.bind('1', step1)
    new.bind('2', step2)
    new.bind('3', step3)
    new.bind('4', step4)
    new.bind('5', step5)
    test.pack(padx=15, pady=15, ipadx=15, ipady=15)
    # end of top frame stuff

    # midframe begins
    Label(midframe, text="Current X and Y Positions Seperated by a Space",font=(
        "Helvetica", 15), borderwidth=1, relief="solid", bg="white", fg="black").pack()
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
    Label(botframe,text="Finally make sure the above point are accurate x and y points",
              font=("Helvetica", 20)).pack()
    Label(botframe,text="DONT FORGET TO",
              font=("Helvetica", 20)).pack()
    Label(botframe,text="Press save or you will have to redo this again!!!!",
              font=("Helvetica", 20)).pack()
    ttk.Button(botframe,text='SAVE',command=saveData).pack()   
    ttk.Button(botframe, text='Close', command=new.destroy).pack(
        padx=10, pady=10, ipadx=20, ipady=60)
    # buttom frame ends
    new.grab_set()

#N/A comment keypress function
def keyboard_press(): 
    #pyautogui.moveTo(1000,1000);pyautogui.dragTo(button='left')
    #pyautogui.moveTo(colorPos[0],colorPos[1])
    #pyautogui.click(colorPos,button='left')
    pyautogui.click(colorPos,button='left')
    pyautogui.click(purplePos, button = 'left')
    #pyautogui.doubleClick()
    #This is the purple color ^
    pyautogui.click(commentPos); pyautogui.typewrite("N/A")
    pyautogui.click(savePos, button = 'left')
    pyautogui.click(locationPos, button = 'left')
    #tempDisplay()

#DOT? comment keypress function
def keyboard_press2():
    #pyautogui.moveTo(1000,1000);pyautogui.dragTo(button='left')
    #pyautogui.moveTo(colorPos[0],colorPos[1])
    #pyautogui.click(colorPos,button='left')
    pyautogui.click(colorPos,button='left')
    pyautogui.click(purplePos, button = 'left')
    #pyautogui.doubleClick()
    #This is the purple color ^
    pyautogui.click(commentPos); pyautogui.typewrite("DOT?")
    pyautogui.click(savePos, button = 'left')
    pyautogui.click(locationPos, button = 'left')
    #tempDisplay()

#Broken comment keypress function
def keyboard_press3():
    #pyautogui.moveTo(1000,1000);pyautogui.dragTo(button='left')
    #pyautogui.moveTo(colorPos[0],colorPos[1])
    #pyautogui.click(colorPos,button='left')
    pyautogui.click(colorPos,button='left')
    pyautogui.click(purplePos, button = 'left')
    #pyautogui.doubleClick()
    #This is the purple color ^
    pyautogui.click(commentPos); pyautogui.typewrite("Broken")
    pyautogui.click(savePos, button = 'left')
    pyautogui.click(locationPos, button = 'left')
    #tempDisplay()

# def open_run(): #opens new windown to run script
#     run = Toplevel(win)
#     run.geometry("300x300")
#     run.title("SCRIPT RUNNING")
#     Label(run,text='Script is running, press 1 to collect data.',font=('Helvetica 15 ')).pack(pady=5)
#     Label(run,text='Press the close button below to end',font=('Helvetica 15 ')).pack(pady=5)
#     #print(colorPos[1])
#     # run.bind('1',keyboard_press)
#     # run.bind('2',keyboard_press2)
#     # run.bind('3',keyboard_press3)
#     ttk.Button(run, text='Close', command=run.destroy).pack(
#         padx=10, pady=10, ipadx=20, ipady=60)
#     # buttom frame ends
#     run.grab_set()
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

def saveData(): #use to save position data
    data = []
    data.append(colorPos)
    data.append(purplePos)
    data.append(commentPos)
    data.append(savePos)
    data.append(locationPos)
    print(data)
    file = open('setupData', 'wb')
    pickle.dump(data, file)
    file.close()
    print("successfully saved everything!")

def openData(): #load in position data after starting program
    file = open('setupData', 'rb')
    data = pickle.load(file)
    file.close()
    global colorPos, purplePos,commentPos,savePos,locationPos
    colorPos = data[0]
    purplePos = data[1]
    commentPos = data[2]
    savePos = data[3]
    locationPos = data[4]
    #Label(win,text="Loaded saved data successfully, You can start script")
    print("finished loading data!")
    tempDisplay()

def tempDisplay(): # use to test in terminal
    print("color postion: ", colorPos)
    print("purple postion: ", purplePos)
    print("comment postion: ", commentPos)
    print("save postion: ", savePos)
    print("location button: ", locationPos)
############# End of Helpers ##################

tempDisplay()
# Create a label
Label(win, text="Click the below button to start set up",
      font=('Helvetica 15')).pack()
Label(win, text="If you successfully did setup skip to load data").pack()
# Create a button to open a New Windows
ttk.Button(win, text='Set Up Tutortial', command=open_win).pack(pady=5)
Label(win, text="MUST LOAD OLD DATA FIRST or script won't work",
      font=('Helvetica 15 bold')).pack()
Label(win, text="Click Load button to load saved data",
      font=('Helvetica 15 ')).pack()
ttk.Button(win, text='Load', command=openData).pack(pady=5)
Label(win, text="Now you can click the button below to run program",
      font=('Helvetica 15 ')).pack()
ttk.Button(win, text='RUN SCRIPT', command=win.destroy).pack(pady=5)
Label(win,text='Press 1 key to collect and write N/A',font=('Helvetica 15 ')).pack(pady=5)
Label(win,text='Press 2 key to collect and write DOT?',font=('Helvetica 15 ')).pack(pady=5)
Label(win,text='Press 3 key to collect and write broken',font=('Helvetica 15 ')).pack(pady=5)
Label(win,text='Press the esc key to exit script',font=('Helvetica 15 ')).pack(pady=5)
#ttk.Button(win, text='Close', command=win.destroy).pack(
    #padx=10, pady=10, ipadx=20, ipady=60)
win.mainloop()

#********************************#
'''
Next steps: 

-edit readme file with steps you might need to start up etc

-document the code and make exe file to see if it works on both mac and windows

-figure out how to send out exe file

-need to figure out how to run this in the background so it works without
having to constantly open the window

-make a video tutorial of how to start up
'''

def methods():
    key = keyboard.read_key()

    if key == '1':
        print("Option {} was pressed\n".format(key))
        keyboard_press()
    elif key == '2':
        print("Option {} was pressed\n".format(key))
        keyboard_press2()
    elif key == '3':
        print("Option {} was pressed\n".format(key))
        keyboard_press3()
    elif key == 'esc':
        print("Exiting the script.........\n")
        exit(0)
    else :
        print("Invalid key\n")


print('press 1 for N/A')
print('press 2 for DOT?')
print('press 3 for Broken')
print('press esc key to exit')

while (True):
    methods()
    #time.sleep(6)
