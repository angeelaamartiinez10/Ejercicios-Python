from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk  #para combobox

usuario=""
contraseña1=""
contraseña2=""
vUsuario=[]

def guardarDatos():
    usuario=datos_usuario.get()
    contraseña1=datos_contraseña1.get()
    contraseña2=datos_contraseña2.get()
    if contraseña1==contraseña2:
        vUsuario.append(usuario)
        vUsuario.append(contraseña1)
        datos_usuario.delete(0,len(usuario))
        datos_contraseña1.delete(0,len(contraseña1))
        datos_contraseña2.delete(0,len(contraseña2))
        messagebox.showinfo("Usuario guardado", "usuario",usuario,"guardado correctamente")
    else:
        print("Las contraseñas no coinciden")
    print(usuario + "-" + contraseña1)
    print(vUsuario)

ventana=Tk()

ventana.title("Almacenamiento de datos")
ventana.geometry("500x300")
ventana.resizable(width=False,height=False)
ventana.config(background="lavender")

label_titulo=ttk.Label(ventana, text="Datos del usuario")

label_usuario=ttk.Label(ventana, text="Nombre de ususario")
datos_usuario=ttk.Entry(ventana)


label_contraseña1=ttk.Label(ventana, text="Contraseña")
datos_contraseña1=ttk.Entry(ventana,show="*")


label_contraseña2=ttk.Label(ventana, text="Repite la contraseña")
datos_contraseña2=ttk.Entry(ventana,show="*")

boton_guardar=ttk.Button(ventana,text="Guardar", command=guardarDatos)
boton_salir=ttk.Button(ventana,text="Salir",command=ventana.destroy)


        #DISTRIBUCION

label_titulo.grid(row=0,column=0,pady=20,padx=20)
label_usuario.grid(row=1,column=1,pady=8,padx=8)
label_contraseña1.grid(row=2,column=1,pady=8,padx=8)
label_contraseña2.grid(row=3,column=1,pady=8,padx=8)

datos_usuario.grid(row=1,column=2,pady=8)
datos_contraseña1.grid(row=2,column=2,pady=8)
datos_contraseña2.grid(row=3,column=2,pady=8)

boton_guardar.grid(row=5,column=1,pady=30)
boton_salir.grid(row=5,column=2,pady=30)


'''COMBOBOX'''

combo = ttk.Combobox(ventana,
    state="readonly",
    values=["Mujer", "Hombre"])
combo.grid(row=4,column=2,pady=20)
combo.set("Selecciona una opcion")



ventana.mainloop()