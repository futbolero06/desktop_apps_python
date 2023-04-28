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

ventana_principal.title ( "Bandera De Colombia")


# tamaño de la ventana
ventana_principal.geometry ("500x500")

# desabilitar el botón maximizar

ventana_principal.resizable(False,False)

#color de fondo de la ventana
ventana_principal.config(bg="black")


#---------------------------
# Frame amarillo
#---------------------------

Frame_amarillo = Frame (ventana_principal)
Frame_amarillo.config(bg="yellow", width=500, height=250)
Frame_amarillo.place(x=0,y=0)

Frame_blue = Frame (ventana_principal)
Frame_blue.config(bg="blue", width=500, height=125)
Frame_blue.place(x=0,y=250)

Frame_rojo = Frame (ventana_principal)
Frame_rojo.config(bg="red", width=500, height=125)
Frame_rojo.place(x=0,y=375)


#run
# se ejcuta el mérojonloop ()de la clase tk ()a traves de la instancia ventana_principal.Este método despliega la ventana en pantalla y queda a la espera de lo que el usuario aga (click en un botón, escribir. etc) . cada acción del usuario se conoce como un evento. El método mainloop () es un bucle infinito.run
ventana_principal.mainloop()