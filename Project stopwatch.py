from tkinter import *
import datetime
import time

b = datetime.datetime.now()
bb = str(b)
print('Start on {0}'.format(bb))

def timess():
    try:
        a = datetime.datetime.now()
        c = a-b
        lbl.configure(text = a)
        lbll.configure(text = c)
    except:
        print('Ошибка!')

root = Tk()

root.title('Time')
root['bg'] = 'white'
root.geometry('265x60')

root.lift()
root.attributes("-topmost", True)

root.resizable(width=False, height=False)

lbl = Label(root, text='1', font= ('Arial', 15), bg="white")
lbl.grid(column = 0, row = 0)
lbll = Label(root, text='2', font= ('Arial', 15), bg="white")
lbll.grid(column = 0, row = 1)

while True:
    try:
        timess()
        root.update()
    except:
        print('Ошибка!')
        exit()

