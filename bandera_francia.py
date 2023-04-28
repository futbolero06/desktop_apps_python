#---------------------
# Desktop app No.1
#---------------------

# se importa la libreria de tkinter con todas sus funciones 
from tkinter import *


#-------------------------
# funciones de la app
#------------------------


#-----------------------------
#ventana principal de la app
#---------------------------

# se declara una variable llamada ventana_principal, que adquiere las cracteristicas de un objeto Tk
ventana_principal = Tk()

# titulo de la ventana

ventana_principal.title ( "Bandera De Francia")


# tamaño de la ventana
ventana_principal.geometry ("600x600")

# desabilitar el botón maximizar

ventana_principal.resizable(False,False)

#color de fondo de la ventana
ventana_principal.config(bg="black")


#---------------------------
# Frame amarillo
#---------------------------

Frame_white = Frame (ventana_principal)
Frame_white.config(bg="white", width=200, height=600)
Frame_white.place(x=200,y=0)

Frame_blue = Frame (ventana_principal)
Frame_blue.config(bg="blue", width=200, height=600)
Frame_blue.place(x=00,y=0)

Frame_rojo = Frame (ventana_principal)
Frame_rojo.config(bg="red", width=200, height=600)
Frame_rojo.place(x=400,y=0)
ventana_principal.mainloop()
