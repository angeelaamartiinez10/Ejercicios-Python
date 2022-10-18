#Listas python

vNombres = [] #se pone cuando queremos poner una lista

#Insertar un dato
vNombres.insert(0,"Juan")
vNombres.insert(1,"Pepe")
vNombres.insert(2,"Ines")
vNombres.append("Minerva") #se añade al final
vNombres.insert(1,"Julian")

#Eliminar elementos
#vNombres.clear()  ->> elimina toda la fila
vNombres.remove("Pepe")    #->> busca y elilmina un dato de la fia
#vNombres.pop(1)  ->>busca y elimina un dato
print("El nombre borrado es", vNombres.pop(1))

#Ordenar una lista
vNombres.sort() #ordena la lista
vNombres.sort(reverse=True)#ordena del reves

#contar el numero de elementos de la lista
vNombres.count("Pepe")
print("Ines aparece "vNombres.count("Ines"))
print("La lista tiene", len(vNombres))


print(vNombres)