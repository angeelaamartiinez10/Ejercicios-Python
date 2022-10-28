#Funciones definidas por el ususario

from pytube import YouTube  #para entrar en la carpeta descargada
from pytube import Playlist

def imprimirHola(nombre:str, apellido:str): #nombre del tipo string(palabra)
    print("Hola",nombre, ""  , apellido)

imprimirHola("Angela","Martínez")  #es el nombre qeu se ha guardado como si fuerna nombre=angela

#ejercicio

def suma(num1:int,num2:int):
    print("La suma es = ",num1+num2)
    return num1+num2   #devuelve la suma

sumar=(suma(1,2))  
print ("la suma es:" ,sumar)  

def descargarCancion(url:str):
    youtube = YouTube(url)
    youtube.authorplaylist
    print(youtube.author)
    print ("Descargando", youtube.title)
    cancion=youtube.streams.get_audio_only()
    cancion.download()
    
def descargarLista(url:str):
    playlist = Playlist(url)
    for cancion in playlist.videos:
        print("Descargando cancion: ",cancion.title)
        cancion.streams.get_audio_only().download("canciones/")
        print ("*****************\n")
url="https://www.youtube.com/playlist?list=PL68B86C1DFA80AA8F"
descargarLista(url)


#descargarCancion("https://www.youtube.com/watch?v=UYXULc8E5fs&list=RDUYXULc8E5fs&start_radio=1")
