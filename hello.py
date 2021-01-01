import pyautogui
import tkinter as tk
import os, fnmatch
global mySeq
mySeq = []

root = tk.Tk()

canvas1 = tk.Canvas(root, width = 150, height = 40)
canvas1.pack()
"""
def hello():
    label1 = tk.Label(root, text='Hellow  World!', fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)

button1 = tk.Button(text='Click Me', command=hello, bg='brown', fg='white')
canvas1.create_window(150, 150, window=button1)
"""

def checkSeq():
    mySeq.clear()
    listOfFiles = os.listdir(r'.\Test\\')
    pattern = 'Image*.png'
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            # mySeq.append(entry)
            mySeq.append(eval(entry[5:entry.find('.')]))
            mySeq.sort()                
    print('Starting...')
    myList = ['...']
    myList.extend(mySeq[-10:])
    print(myList)
                             

def takeScreenshot():
    myScreenshot = pyautogui.screenshot()
    if mySeq: #len(mySeq) != 0:
        pass #print(max(mySeq)+1)
    else:
        mySeq.append(0)
    myScreenshot.save(r'C:\\Users\Janardan\Desktop\MyPython\Test\Image' + str(max(mySeq)+1) + '.png')
    checkSeq()

    
checkSeq()

myButton = tk.Button(text='Go', command=takeScreenshot, bg='green', fg='white', font=10)
canvas1.create_window(75, 20, window=myButton)

#print(max(mySeq)+1)

root.mainloop()



