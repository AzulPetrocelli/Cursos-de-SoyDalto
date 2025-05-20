#FUNCIONES---------------------------------------------

#Crear una lista, no se usa mucho pero es bueno para crear una lista vacia
lista = list(["Hola", "Azul", 22])

#Crear un conjunto
conjunto = set(["Hola", "Azul", 22])

#Cantidad de elementos de una lista
cantidad_de_elementos = len(lista) #3

#Retornar metodos y/o funciones que puede usar una lista, conjunto o tupla
print(dir(lista))
print(dir(conjunto))
print(dir("Tupla", "ejemplo"))

#METODOS---------------------------------------------

#Agregar un elemento a la lista al final
lista.append("Petrocelli")

#Agregar un elemento a la lista en un indice especifica
lista.insert(2, "Martin")

#Agregar varios elementos al final de la lista, es como una concatenacion de listas
lista.extend([False, 2025])

#Eliminar un elemento de la lista por indice
lista.pop(3) #-1 se elimina el ultimo, -2 se elimina el anteultimo y asi sucesivamente

#Remover un elemento por su valor
lista.remove(False) #Si no encuentra el valor lanza una excepcion

#Eliminar todos los elementos de la lista
#lista.clear()

lista = [0,1,2,3, True,4,5,6,False]
#Ordenar lista de forma ascendente(si usamos el parametro reverse=True lo ordena de forma decendente)
lista.sort(reverse=False) #lista.sort()
lista.sort(reverse=True)

#invertir los elementos de la lista (no los ordena decendentemente)
lista.reverse()

print(lista)