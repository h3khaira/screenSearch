import pyautogui as g
import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()


def takeScreenshot():
    myScreenshot = g.screenshot(region=(0, 0, 300, 400))
    myScreenshot.save('screenshot.jpg')
    root.quit()


def regionSelect():
    print("test")


myButton1 = tk.Button(text='Select Region',
                      command=regionSelect,
                      bg='green',
                      fg='white',
                      font=10)

myButton2 = tk.Button(text='Take Screenshot',
                      command=takeScreenshot,
                      bg='blue',
                      fg='white',
                      font=10)

canvas1.create_window(150, 150, window=myButton1)
canvas1.create_window(150, 50, window=myButton2)

root.mainloop()
