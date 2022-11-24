from tkinter import *
from tkinter import ttk

ventana=Tk()

ventana.title("Almacenamiento de datos")
ventana.geometry("500x300")
ventana.resizable(width=False,height=False)
ventana.config(background="lavender")

label_titulo=ttk.Label(ventana, text="Datos del usuario")

label_usuario=ttk.Label(ventana, text="Nombre de ususario")


datos_usuario=ttk.Entry(ventana)


label_contraseña1=ttk.Label(ventana, text="Contraseña")

datos_contraseña1=ttk.Entry(ventana)


label_contraseña2=ttk.Label(ventana, text="Repite la contraseña")

datos_contraseña1=ttk.Entry(ventana)
datos_contraseña2=ttk.Entry(ventana)

boton_guardar=ttk.Button(ventana,text="Guardar",)
boton_salir=ttk.Button(ventana,text="Salir",)



label_titulo.grid(row=0,column=0)
label_usuario.grid(row=1,column=1)
label_contraseña1.grid(row=2,column=1)
label_contraseña2.grid(row=3,column=1)

datos_usuario.grid(row=1,column=2)
datos_contraseña1.grid(row=2,column=2)
datos_contraseña2.grid(row=3,column=2)

boton_guardar.grid(row=20,column=3)
boton_salir.grid(row=25,column=3)



ventana.mainloop()