from tkinter import *
from tkinter import ttk


def saludar():
    texto= campoTexto.get()    #devuleve el texto
    textoLabel.set(texto)
    print(texto)

#generar la ventana
ventana = Tk()
ventana.title("Primer ejercicio")
ventana.geometry("400x500")
ventana.resizable(width=False,height=False)
ventana.config(background="light blue")

#genera el lienzo para pintar componentes
frm = ttk.Frame(ventana).pack()  #padding->> anchura de la ventana



#componentes label y button

textoLabel=StringVar()
textoLabel.set("Hola Tkinter")
labelTexto=ttk.Label(frm, textvariable=textoLabel)
labelTexto.config(background="sky blue", border=5, font=("arial",15))  #label--->> texto
labelTexto.pack()

#componente cuadro de texto
campoTexto= ttk.Entry(frm)
campoTexto.pack()  #barra para escribir




ttk.Button(frm, text="Saludo", command=saludar).pack()     
ttk.Button(frm, text="Salir", command=ventana.destroy).pack()      # command-->> nombrar. destroy-->> cierra la ventana



ventana.mainloop()  # bucle que hace que se presente en la vantana
