from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Carrusel de imagenes')

img1 = ImageTk.PhotoImage(Image.open('C:/Users/JCH/Desktop/Pyproyectos/TkInter/carrusel/images/01.jpg'))
img2 = ImageTk.PhotoImage(Image.open('C:/Users/JCH/Desktop/Pyproyectos/TkInter/carrusel/images/02.jpg'))
img3 = ImageTk.PhotoImage(Image.open('C:/Users/JCH/Desktop/Pyproyectos/TkInter/carrusel/images/03.jpg'))
img4 = ImageTk.PhotoImage(Image.open('C:/Users/JCH/Desktop/Pyproyectos/TkInter/carrusel/images/04.jpg'))
img5 = ImageTk.PhotoImage(Image.open('C:/Users/JCH/Desktop/Pyproyectos/TkInter/carrusel/images/05.jpg'))
img6 = ImageTk.PhotoImage(Image.open('C:/Users/JCH/Desktop/Pyproyectos/TkInter/carrusel/images/06.jpg'))

lista = [img1, img2, img3, img4, img5, img6]

l = Label(root, image=img1)
l.grid(row=0, column=0, columnspan=3)

def adelante(img_num):
    global l
    global boton_adelante
    global boton_atras

    l.grid_forget()
    l = Label(root, image=lista[img_num])
    boton_atras = Button(root, text='<-', command=lambda: atras(img_num - 1))
    boton_adelante = Button(root, text='->', command=lambda: adelante(img_num + 1))

    if img_num == (len(lista) - 1):
        boton_adelante= Button(root, text='N/A', state=DISABLED)

    l.grid(row=0, column=0, columnspan=3)
    boton_atras.grid(row=1, column=0)
    boton_adelante.grid(row=1, column=2)

def atras(img_num):
    global l
    global boton_adelante
    global boton_atras

    l.grid_forget()
    l = Label(root, image=lista[img_num])
    boton_atras = Button(root, text='<-', command=lambda: atras(img_num - 1))
    boton_adelante = Button(root, text='->', command=lambda: adelante(img_num + 1))

    if img_num == 0:
        boton_atras= Button(root, text='N/A', state=DISABLED)

    l.grid(row=0, column=0, columnspan=3)
    boton_atras.grid(row=1, column=0)
    boton_adelante.grid(row=1, column=2)

boton_atras = Button(root, text='N/A', state=DISABLED)
boton_adelante = Button(root, text='->', command=lambda: adelante(1))

boton_atras.grid(row=1, column=0)
boton_adelante.grid(row=1, column=2)

root.mainloop()