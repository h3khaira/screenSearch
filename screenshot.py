import pyautogui as g
import tkinter as tk

startx = 0
starty = 0
endx = 0
endy = 0

root = tk.Tk()
# settings for the transparent window on which the screenshot region is selected

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()


def mouseClick(mouseEvent):
    print("clicked at ", mouseEvent.x, mouseEvent.y)
    startx = mouseEvent.x
    starty = mouseEvent.y


def mouseRelease(mouseEvent, rootToClose, rootToMax):
    print("released at ", mouseEvent.x, mouseEvent.y)
    endx = mouseEvent.x
    endy = mouseEvent.y
    rootToClose.destroy()
    rootToMax.wm_state("normal")


def takeScreenshot():
    # myScreenshot = g.screenshot(region=(startx, starty, endx, endy))
    myScreenshot = g.screenshot(region=(216, 225, 783, 593))
    myScreenshot.save('screenshot.jpg')
    root.quit()


def regionSelectMode():
    # minimize the window containing the buttons
    root.wm_state('iconic')

    rootTransparent = tk.Tk()
    # change the alpha value to change the transparency of the screenshot region selection window
    rootTransparent.attributes('-alpha', 0.05)
    regionWindow = tk.Canvas(rootTransparent,
                             width=rootTransparent.winfo_screenwidth(),
                             height=rootTransparent.winfo_screenheight())
    regionWindow.bind("<Button-1>", mouseClick)
    regionWindow.bind("<ButtonRelease-1>",
                      lambda event: mouseRelease(event, rootTransparent, root))
    regionWindow.pack()
    rootTransparent.mainloop()


# pressing this button will make the program go into region select mode
myButton1 = tk.Button(text='Select Region',
                      command=regionSelectMode,
                      bg='green',
                      fg='white',
                      font=10)

# this button should activate the screenshot save then search it on google
myButton2 = tk.Button(text='Take Screenshot',
                      command=takeScreenshot,
                      bg='blue',
                      fg='white',
                      font=10)

canvas1.create_window(150, 150, window=myButton1)
canvas1.create_window(150, 50, window=myButton2)

root.mainloop()
