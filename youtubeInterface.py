from tkinter import *
from tkinter import ttk

from pytube import YouTube 
from pytube import Playlist

def descargarCancion ():
    url= datos_entrada.get()
    youtube=YouTube(url)
    cancion=youtube.streams.get_audio_only()
    cancion.download()


ventana= Tk()
ventana.title("Descargar música :)))")
ventana.geometry("700x150")
ventana.resizable(width=False,height=False)
ventana.config(background="light blue")


datos_entrada=ttk.Entry(ventana)
datos_entrada.place(x=265, y=50)

boton_descargar=ttk.Button(ventana,text="Descargar",command=descargarCancion)
boton_descargar.place(x=305, y=90)


label_titulo=ttk.Label(ventana, text="***Introduce la URL del video***")
label_titulo.place(x=210, y=10)
label_titulo.config(background="cornflowerblue", border=5, font=("times new roman",15))  #label--->> texto



ventana.mainloop()