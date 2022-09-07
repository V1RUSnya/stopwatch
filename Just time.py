from tkinter import *
import datetime

b = datetime.datetime.now().time()
bb = str(b)
print('Start on ' + bb)

def timess():
    a = datetime.datetime.now().time()
    lbl.configure(text = a)

root = Tk()

root.title('Time')
root.geometry('160x35')

root.resizable(width=False, height=False)

lbl = Label(root, text='1', font= ('Arial', 15))
lbl.grid(column = 0, row = 0)

while True:
    timess()
    root.update()

