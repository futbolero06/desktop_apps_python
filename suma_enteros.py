
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
ventana_principal.config(bg="blue")


#---------------------------
# Frame entrada datos
#---------------------------

Frame_entrada = Frame (ventana_principal)
Frame_entrada.config(bg="white", width=480, height=180)
Frame_entrada.place(x=10,y=10)

Frame_white  = Frame (ventana_principal)
Frame_white .config(bg="white", width=480, height=125)
Frame_white .place(x=10,y=200)



# logo de la app
logo = PhotoImage ( file="img/escudo_colegio.png")
lb_logo= Label (Frame_entrada, image=logo,bg="white")
lb_logo.place(x=70,y=40)

# titulo de la app
titulo = Label (Frame_entrada, text="suma Enteros 1.0 ")
titulo.config(bg="white", fg="blue", font=("Helvetica", 20))
titulo.place(x=240,y=10)

#etiqueta para el valor x
lb_x = Label (Frame_entrada, text="X =  ")
lb_x.config(bg="white", fg="blue", font=("Helvetica", 18))
lb_x.place(x=240, y=60)

#caja de texto para valor x
entry_x = Entry (Frame_entrada)
entry_x.config(bg="white", fg= "blue", font=("Times New Roman", 18), width=6)
entry_x.focus_set()
entry_x.place(x=290,y=60)

#etiqueta para el valor y
lb_y = Label (Frame_entrada, text="Y = ")
lb_y.config(bg="white", fg="blue", font=("Helvetica", 18))
lb_y.place(x=240, y=120)

#caja de texto para valor y
entry_y = Entry (Frame_entrada)
entry_y.config(bg="white", fg= "blue", font=("Times New Roman", 18), width=6)
entry_y.place(x=290,y=120)
#---------------------------
# Frame operaciones
#---------------------------
Frame_white  = Frame (ventana_principal)
Frame_white .config(bg="white", width=480, height=155)
Frame_white .place(x=10,y=335)



#run
ventana_principal.mainloop()