import pyautogui as g
import tkinter as tk
from pynput import mouse

startx = 0
starty = 0
endx = 0
endy = 0

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()


def mouse_click(x, y, button, pressed):
    if pressed:
        startx = x
        starty = y
    if not pressed:
        endx = x
        endy = y


def takeScreenshot():
    myScreenshot = g.screenshot(region=(startx, starty, endx, endy))
    myScreenshot.save('screenshot.jpg')
    root.quit()


def regionSelect():
    # non-blocking event listener for mouse clicks
    listener = mouse.Listener(on_click=mouse_click)
    listener.start()


# pressing this button will make the program go into region select mode
myButton1 = tk.Button(text='Select Region',
                      command=regionSelect,
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
