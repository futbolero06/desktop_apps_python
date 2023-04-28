#bandera de españa
# se importa la libreria de tkinter con todas sus funciones 
from tkinter import *


#-------------------------
# funciones de la app
#------------------------

ventana_principal = Tk()
ventana_principal.title ( "Bandera De españa")
ventana_principal.geometry ("600x600")


Frame_red = Frame (ventana_principal)
Frame_red.config(bg="red", width=600, height=150)
Frame_red.place(x=0,y=0)

Frame_yellow = Frame (ventana_principal)
Frame_yellow.config(bg="yellow", width=600, height=300)
Frame_yellow.place(x=0,y=150)


Frame_red = Frame (ventana_principal)
Frame_red.config(bg="red", width=600, height=150)
Frame_red.place(x=00,y=450)

Frame_black = Frame (ventana_principal)
Frame_black.config(bg="black", width=100, height=100)
Frame_black.place(x=200,y=250)

ventana_principal.mainloop()
