from tkinter import *
from tkinter import ttk

#generar la ventana
ventana = Tk()
ventana.title("Primer ejercicio")
ventana.geometry("400x500")
ventana.resizable(width=False,height=False)
ventana.config(background="light blue")
ventana.iconbitmap()

#genera el lienzo para pintar componentes
frm = ttk.Frame(ventana).pack()  #paddinf->> anchura de la ventana


#componentes label y button
labelTexto=ttk.Label(frm, text="Hola Tkinter!")
labelTexto.config(background="sky blue", border=5, font=("arial",15))  #label--->> texto
labelTexto.pack()

ttk.Button(frm, text="Salir", command=ventana.destroy).pack()      # command-->> nombrar. destroy-->> cierra la ventana

ventana.mainloop()  # bucle que hace que se presente en la vantana
