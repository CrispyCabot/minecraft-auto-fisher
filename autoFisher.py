#autoFisher.py

import pyautogui as pag
import time
from PIL import Image, ImageGrab
import keyboard
from tkinter import *

def autoFish():
    time.sleep(3)
    size = int(sizeVal.get())
    x, y = pag.position()
    print("PAG LOC: ", x, y)
    img = ImageGrab.grab(bbox=(x-size, y-size, x+size, y+size)) #bbox specifies specific region (bbox= x,y,width,height)

   # img.show()
    counter = 1
    running = True
    while running:
        print("Image ", counter)
        img = ImageGrab.grab(bbox=(x-size, y-size, x+size, y+size)) #bbox specifies specific region (bbox= x,y,width,height)
        if checkWhite(img):
            print("found white")
        else:
            pag.rightClick()
            time.sleep(0.5)
            pag.rightClick()
            time.sleep(2)
        counter += 1
        if keyboard.is_pressed("ctrl"):
            running = False
        if counter % 100 == 0:
            print("Drawing new image")
            img.save("lastImg.gif")
            imgg = PhotoImage(file="lastImg.gif")
            window.create_image(winWidth/2, winHeight-75, image=imgg, anchor="center")
            window.update()
      
def checkWhite(img):
    size = int(sizeVal.get())
    nearWhite = int(whiteVal.get()) #skew of how white to look for - looks for white bobber rgb scale of 0-255 255,255,255 is perfect white
    for x in range(0, size*2):
        for y in range(0, size*2):
            i = img.getpixel((x, y))
            if i[0] > nearWhite and i[1] > nearWhite and i[2] > nearWhite:
              #  print("Found color: ", i) #all the rgb values met nearwhite criteria
                return True
    return False

size = 35
winHeight = 250
winWidth = 500

win = Tk()
win.resizable(False, False)
window = Canvas(win)

window.pack(side="left", fill=BOTH, expand=True)

win.title("Minecraft Auto Fisher")

win.geometry(str(winWidth)+'x'+str(winHeight))

colX = [winWidth/2-10, winWidth/2+10]

#Start Button
start = Button(window, width="45", text="Start Auto Fisher", bg="blue", fg="lightgreen", activebackground="green", activeforeground="white", command=autoFish)
start.place(x=winWidth/2, y=20, anchor="center")

#Near White label and entry
Label(window, text="White Skew: ").place(x=colX[0], y=50, anchor="e")
whiteVal = Entry(window, width=5)
whiteVal.place(x=colX[1], y=50, anchor="w")
whiteVal.insert(0, "200")

#Draw Size Label and entry
Label(window, text="Image Grab Size: ").place(x=colX[0], y=75, anchor="e")
sizeVal = Entry(window, width=5)
sizeVal.place(x=colX[1], y=75, anchor="w")
sizeVal.insert(0, 35)

#Draw last img test
Label(window, text="Last Image (You want the bobber to be as low in the image as possible):").place(x=winWidth/2, y=115, anchor="center")
#img = PhotoImage(file="lastImg.gif")
#window.create_image(winWidth/2, winHeight-75, image=img, anchor="center")

window.mainloop()