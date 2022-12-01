from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk





ventana=Tk()


ventana.title("Lista de la compra")
ventana.geometry("500x500")
ventana.resizable(width=False,height=False)
ventana.config(background="lavender")


combo = ttk.Combobox(ventana,
    state="readonly",
    values=["Verduras", "Carne"])
combo.grid(row=1,column=1,pady=1)
combo.set("Selecciona una opcion")

#boton_guardar=ttk.Button(ventana,text="Guardar", command=guardarDatos)




ventana.mainloop()