#bandera de noruega
# se importa la libreria de tkinter con todas sus funciones 
from tkinter import *


#-------------------------
# funciones de la app
#------------------------

ventana_principal = Tk()
ventana_principal.title ( "Bandera De Noruega")
ventana_principal.geometry ("800x600")


Frame_red = Frame (ventana_principal)
Frame_red.config(bg="red", width=800, height=600)
Frame_red.place(x=0,y=0)

frame_white= Frame (ventana_principal)
frame_white.config(bg="white", width=100, height=600)
frame_white.place (x=200,y=0)


frame_white= Frame (ventana_principal)
frame_white.config(bg="white", width=800, height=100)
frame_white.place (x=0,y=250)

frame_blue= Frame (ventana_principal)
frame_blue.config(bg="midnight blue", width=50, height=600)
frame_blue.place (x=225,y=0)


frame_blue= Frame (ventana_principal)
frame_blue.config(bg="midnight blue", width=800, height=50)
frame_blue.place (x=0,y=275)







ventana_principal.mainloop()