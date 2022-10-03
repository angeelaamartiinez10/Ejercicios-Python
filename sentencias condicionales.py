# Sentencias condicionales

#Ejercicio 1. Leer por teclado tu edad e imprima por pantalla si eres mayor o menor

edad=0

edad=(int)(input("¿Cúantos años tienes?"))  #int para que no te de error al poner un numero
if(edad>=18):
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")