#Creando un conjunto con set()
conjunto = set(["Dato 1", "Dato 2"])

#IMPORTANTE: dentro de los conjuntos no pueden ir datos variables como 
# las listas o diccionarios pero las tuplas y otros conjuntos INMUTABLES

#Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato 1", "dato 2"]) #creamos un conjunto inmutable
conjunto2 = {conjunto1, "dato 3"}

#Teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,6}

#Subconjunto: grupo de valores que estan incluidos en un Conjunto
resultado = conjunto2.issubset(conjunto1) #True
resultado = conjunto2 <= conjunto1 #True --> otra forma de escribir lo de arriba

resultado = conjunto1.issubset(conjunto2) #False
resultado = conjunto1 <= conjunto2 #False

#SuperConjunto: grupo de valores que incluyen los del Conjunto y mas
resultado = conjunto2.issuperset(conjunto1) #False
resultado = conjunto2 > conjunto1 #True --> otra forma de escribir lo de arriba

resultado = conjunto1.issuperset(conjunto2) #True
resultado = conjunto1 > conjunto2 #False

#Verificar si hay al menos un elemento en comun
resultado = conjunto2.isdisjoint(conjunto1)