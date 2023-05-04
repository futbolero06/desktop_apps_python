
# se importa la libreria tkiter con todas sus funciones
from tkinter import *
from tkinter import messagebox


#-------------------------
# funciones de la app
#------------------------

#sumar
def calcular():
    messagebox.showinfo("Mini Calculadora 1.0", "Las operaciones han sido realizadas")
    s= int (x.get()) + int(y.get())
    r= int (x.get()) - int(y.get())
    m= int (x.get()) * int(y.get())
    d= int (x.get()) / int(y.get())
    de= int (x.get()) // int(y.get())
    mod= int (x.get()) % int(y.get())
    p= int (x.get()) ** int(y.get())
    t_resultados.insert(INSERT, f" \n {int(x.get())} + {int(y.get())} = {s}")
    t_resultados.insert(INSERT, f" \n {int(x.get())} - {int(y.get())} = {r}")
    t_resultados.insert(INSERT, f" \n {int(x.get())} * {int(y.get())} = {m}")
    t_resultados.insert(INSERT, f" \n {int(x.get())} / {int(y.get())} = {d}")
    t_resultados.insert(INSERT, f" \n {int(x.get())} // {int(y.get())} = {de}")
    t_resultados.insert(INSERT, f" \n {int(x.get())} % {int(y.get())} = {mod}")
    t_resultados.insert(INSERT, f" \n {int(x.get())} ** {int(y.get())} = {p}")

#borrar:
def borrar():
    messagebox.showinfo("Mini Calculadora 1.0", "Los datos serán borrados")
    x.set("")
    y.set("")
    t_resultados.delete("1.0", "end")
    pass

#salir
def salir():
    messagebox.showinfo("Mini Calculadora 1.0", "La app se va a cerrar")
    ventana_principal.destroy()

#salir
#-----------------------------
#ventana principal de la app
#---------------------------

# se declara una variable llamada ventana_principal, que adquiere las cracteristicas de un objeto Tk
ventana_principal = Tk()

# titulo de la ventana

ventana_principal.title ( "Mini Calculadora 1.0")


# tamaño de la ventana
ventana_principal.geometry ("500x500")

# desabilitar el botón maximizar

ventana_principal.resizable(False,False)

#color de fondo de la ventana
ventana_principal.config(bg="blue")
#---------------------------
# variables globales
#---------------------------
x= StringVar()
y= StringVar()

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
entry_x = Entry (Frame_entrada, textvariable=x)
entry_x.config(bg="white", fg= "blue", font=("Times New Roman", 18), width=6)
entry_x.focus_set()
entry_x.place(x=290,y=60)

#etiqueta para el valor y
lb_y = Label (Frame_entrada, text="Y = ")
lb_y.config(bg="white", fg="blue", font=("Helvetica", 18))
lb_y.place(x=240, y=120)

#caja de texto para valor y
entry_y = Entry (Frame_entrada, textvariable=y)
entry_y.config(bg="white", fg= "blue", font=("Times New Roman", 18), width=6)
entry_y.place(x=290,y=120)
#---------------------------
# Frame operaciones
#---------------------------
Frame_operaciones  = Frame (ventana_principal)
Frame_operaciones .config(bg="white", width=480, height=100)
Frame_operaciones .place(x=10,y=200)

#boton para sumar
bt_sumar = Button (Frame_operaciones,text="calcular", command=calcular)
bt_sumar.place(x=45,y=35, width=100, height=30)

#boton para borrar
bt_borrar=Button(Frame_operaciones, text ="Borrar", command=borrar)
bt_borrar.place(x=190,y=35, width=100, height=30)

#boton para salir
bt_salir= Button(Frame_operaciones,text="salir", command=salir)
bt_salir.place(x=335, y=35, width=100, height=30)

#---------------------
# frame resultados
#---------------------



Frame_resultados = Frame(ventana_principal)
Frame_resultados.config(bg="black", width=480, height=300)
Frame_resultados.place(x=10, y=310)


# area de texto para los resultados

t_resultados= Text(Frame_resultados)
t_resultados.config(bg="black" , fg="green yellow", font=("Courier", 18))
t_resultados.place(x=10,y=10, width=460,height=160)
#run
ventana_principal.mainloop()