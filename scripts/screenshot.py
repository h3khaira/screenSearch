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
    global startx, starty
    startx = mouseEvent.x
    starty = mouseEvent.y


def mouseRelease(mouseEvent, rootToClose, rootToMax):
    global endx, endy
    endx = mouseEvent.x
    endy = mouseEvent.y
    rootToClose.destroy()
    rootToMax.wm_state("normal")


def drawRect(moveEvent, window, x1, y1):
    highlightRect = window.create_rectangle(x1,
                                            y1,
                                            moveEvent.x,
                                            moveEvent.y,
                                            outline="black",
                                            fill="black",
                                            width=3)
    window.delete(highlightRect)


def takeScreenshot():
    root.destroy()
    myScreenshot = g.screenshot(region=(startx, starty, abs(endx - startx),
                                        abs(endy - starty)))
    myScreenshot.save('./resources/screenshot.jpg')


def regionSelectMode():
    # minimize the window containing the buttons
    root.wm_state('iconic')

    rootTransparent = tk.Tk()
    # make the window size fixed
    rootTransparent.resizable(width=False, height=False)
    # change the alpha value to change the transparency of the screenshot region selection window
    rootTransparent.attributes('-alpha', 0.05)
    regionWindow = tk.Canvas(rootTransparent,
                             width=rootTransparent.winfo_screenwidth(),
                             height=rootTransparent.winfo_screenheight())
    regionWindow.bind("<Button-1>", mouseClick)

    # draw rectangle to show the user the highlighted region
    regionWindow.bind(
        "<B1-Motion>",
        lambda event: drawRect(event, regionWindow, startx, starty))

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
