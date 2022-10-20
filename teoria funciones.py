#Funciones definidas por el ususario

from pytube import YouTube  #para entrar en la carpeta descargada

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
    youtube.author
    print(youtube.author)
    print ("Descargando", youtube.title)
    cancion=youtube.streams.get_audio_only()
    cancion.download()
    

descargarCancion("https://www.youtube.com/watch?v=UYXULc8E5fs&list=RDUYXULc8E5fs&start_radio=1")
