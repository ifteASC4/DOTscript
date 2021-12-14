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


########### START OF MAIN WINDOW CODE ###########
# Create an instance of tkinter frame or main window
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
########### END OF MAIN WINDOW CODE ###########


########### START OF SET UP TUTORIAL WINDOW ###########
def open_win():  # opens new window for the tutorial
    new = Toplevel(win)
    new.geometry("600x600")#set up window size
    new.title("Set Up Tutorial")
    # Create a Label in New window

    # frames created below to help organzie items
    topframe = Frame(new)
    topframe.pack()
    midframe = Frame(new)
    midframe.pack()
    botframe = Frame(new)
    botframe.pack(side=BOTTOM, pady=20)

    # start of topframe
    # step 1:
    Label(topframe, text="STEP 1: Hover over the color button and press 1",
          font=("Helvetica", 15)).pack()
    # step 2:
    Label(topframe, text="STEP 2: Hover over the purple and press 2",
          font=("Helvetica", 15)).pack()
    # step 3:
    Label(topframe, text="STEP 3: Hover over the comment attribute box and press 3",
          font=("Helvetica", 15)).pack()
    # step 4:
    Label(topframe, text="STEP 4: Hover over the save measurment button and press 4",
          font=("Helvetica", 15)).pack()
    # step 5:
    Label(topframe, text="STEP 5: Hover over the location button and press 5",
          font=("Helvetica", 15)).pack()

    # end of steps/ status 
    test = Label(topframe, text="Current Location Values Below: ", font=(
        "Helvetica", 15), borderwidth=1, relief="solid", bg="white", fg="black")
    #binds number keys and calls corresponding function when key is pressed. 
    new.bind('1', step1)
    new.bind('2', step2)
    new.bind('3', step3)
    new.bind('4', step4)
    new.bind('5', step5)
    test.pack(padx=15, pady=15, ipadx=15, ipady=15)
    # end of top frame stuff

    # midframe begins and shows updates for the keys pressed
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

    # bottom frame begins
    Label(botframe,text="Finally make sure the above point are accurate x and y points",
              font=("Helvetica", 15)).pack()
    Label(botframe,text="DONT FORGET TO",
              font=("Helvetica", 15)).pack()
    Label(botframe,text="Press save or you will have to redo this again!!!!",
              font=("Helvetica", 15)).pack()
    #save data button calls saveData method
    ttk.Button(botframe,text='SAVE',command=saveData).pack(   
        padx=10, pady=10, ipadx=20, ipady=20)
    #close button destroys the new frame (set up frame)   
    ttk.Button(botframe, text='Close', command=new.destroy).pack()
    # bottom frame ends
    new.grab_set()#used so window doesnt close until press close. 
########### END OF SET UP TUTORIAL WINDOW ###########

########### keyboard press methods below ###########
'''
5 steps are done. First it clicks the colorPos then it clicks the color you choose. 
Third the comment postion is clicked and pyautogui writes what ever string you used.
Fourth it clicks the savePos button and finally the location button to save the point.

You can modify the order and add more commands if needed. 
'''
#N/A comment keypress function
def keyboard_press1(): 
    pyautogui.click(colorPos,button='left')
    pyautogui.click(purplePos, button = 'left')
    pyautogui.click(commentPos); pyautogui.typewrite("N/A")
    pyautogui.click(savePos, button = 'left')
    pyautogui.click(locationPos, button = 'left')

#DOT? comment keypress function
def keyboard_press2():
    pyautogui.click(colorPos,button='left')
    pyautogui.click(purplePos, button = 'left')
    pyautogui.click(commentPos); pyautogui.typewrite("DOT?")
    pyautogui.click(savePos, button = 'left')
    pyautogui.click(locationPos, button = 'left')

#Broken comment keypress function
def keyboard_press3():
    pyautogui.click(colorPos,button='left')
    pyautogui.click(purplePos, button = 'left')
    pyautogui.click(commentPos); pyautogui.typewrite("Broken")
    pyautogui.click(savePos, button = 'left')
    pyautogui.click(locationPos, button = 'left')
########### end of keyboard press methods ###########


########### extra stuff may need later?? ###########
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
####################################################


############# START OF HELPER METHODS ###################
'''
step1-5 methods are used to update the global variables with the new points you pick
'''
def step1(event): 
    global colorPos
    colorPos = pyautogui.position()
    colorVar.set(colorPos)#update global pos

def step2(event):
    global purplePos
    purplePos = pyautogui.position()
    purpleVar.set(purplePos)#update global pos

def step3(event):
    global commentPos
    commentPos = pyautogui.position()
    commentVar.set(commentPos)#update global pos

def step4(event):
    global savePos
    savePos = pyautogui.position()
    saveVar.set(savePos)#update global pos

def step5(event):
    global locationPos
    locationPos = pyautogui.position()
    locationVar.set(locationPos)#update global pos

#saveData method takes the global variables for each position and appends it to an array
#then it creates/updates the setupData file to store the values.
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
    print("successfully saved everything!\n")

#openData method loads the variables that were saved using saveData.
#it opens the setupData file and stores them in the global variables 
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
    print("finished loading data!\n")
    tempDisplay()

#this a temp display method used to test and show the values on the terminal
def tempDisplay(): # use to test in terminal
    print("color postion: ", colorPos)
    print("purple postion: ", purplePos)
    print("comment postion: ", commentPos)
    print("save postion: ", savePos)
    print("location button: ", locationPos)
    print()
############# End of Helpers ##################


########### MAIN WINDOW CODE BELOW ###########
tempDisplay()
# Create a label
Label(win, text="Click the below button to start set up",
      font=('Helvetica 15')).pack()
Label(win, text="If you successfully did setup skip to load data").pack()
# Create a button to open a New Windows
#opens the setup tutorial window
ttk.Button(win, text='Set Up Tutortial', command=open_win).pack(pady=5)
Label(win, text="MUST LOAD OLD DATA FIRST or script won't work",
      font=('Helvetica 15 bold')).pack()
Label(win, text="Click Load button to load saved data",
      font=('Helvetica 15 ')).pack()
#load button used to load the data from setupDatat file
ttk.Button(win, text='Load', command=openData).pack(pady=5)
Label(win, text="Now you can click the button below to run program",
      font=('Helvetica 15 ')).pack()
#run script closes the main window so the while loop can start after mainloop() ends
ttk.Button(win, text='RUN SCRIPT', command=win.destroy).pack(pady=5)
Label(win,text='Press 1 key to collect and write N/A',font=('Helvetica 15 ')).pack(pady=5)
Label(win,text='Press 2 key to collect and write DOT?',font=('Helvetica 15 ')).pack(pady=5)
Label(win,text='Press 3 key to collect and write broken',font=('Helvetica 15 ')).pack(pady=5)
Label(win,text='Press the esc key 2 times to exit script',font=('Helvetica 15 ')).pack(pady=5)
#ttk.Button(win, text='Close', command=win.destroy).pack(
    #padx=10, pady=10, ipadx=20, ipady=60)

#bind for escape key must ust lambda function to close window
win.bind('<Escape>',lambda x: win.destroy())
win.mainloop()#closes window and exits the UI
########### END OF MAIN WINDOW CODE ###########
#********************************#

########### CODE RUNS AFTER tkinter window closes ###########
def methods():
    key = keyboard.read_key()#reads the keys pressed

    if key == '1':#if 1 is pressed call keybaord press1
        print("Option {} was pressed\n".format(key))
        keyboard_press1()
    elif key == '2':#if 2 is pressed call keybaord press2
        print("Option {} was pressed\n".format(key))
        keyboard_press2()
    elif key == '3':#if 3 is pressed call keybaord press3
        print("Option {} was pressed\n".format(key))
        keyboard_press3()
    elif key == 'esc': #need to press esc when finished
        print("Exiting the script.........\n")
        exit(0)
    else :
        print("Invalid key\n")

while (True): #runs continuously in the background
    methods()
    time.sleep(1)#wait time about 1 second
########### END OF data collection part###########
