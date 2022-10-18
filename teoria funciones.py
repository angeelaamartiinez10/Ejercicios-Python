#Funciones definidas por el ususario

def imprimirHola(nombre:str, apellido:str): #nombre del tipo string(palabra)
    print("Hola",nombre, ""  , apellido)

imprimirHola("Angela","Martínez")  #es el nombre qeu se ha guardado como si fuerna nombre=angela

#ejercicio

def suma(num1:int,num2:int):
    print("La suma es = ",num1+num2)
    return num1+num2   #devuelve la suma

sumar=(suma(1,2))  
print ("la suma es:" ,sumar)  