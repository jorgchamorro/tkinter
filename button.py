from tkinter import *

root = Tk()
root.geometry('500x500')
root.title('Hola mundo!')

l = Label(root, text='hola mundo')
def click():
    l.pack()

btn = Button(root, text='Clickeame', command=click, fg='red')
btn.pack()


root.mainloop()