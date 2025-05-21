#Todo lo que vamos a hacer funciona tanto 
# para listas como para tuplas y conjutnos

#Conjunto de mascotas
mascotas = {"gato", "perro", "loro", "pez"}

#Tupla con edades
edades = (3, 5, 2, 1)

#Ciclo for
for animal in mascotas:
    print(f"Ahora la variable animal es igual a: {animal}")
    
#Iterar dos o mas listas y/o tuplas y/o conjuntos del mismo tamaño al mismo tiempo
for animal,edad in zip(mascotas,edades):
    print(f"Mi {animal} tiene {edad} años de edad")

#Iterar elementos 5 veces
for num in range(5):
    print(num)

#Iterar elementos en un rango definido de 10 a 20
for num in range(10,20):
    print(num)
    
#Recorrer una lista con su indice
for animal in enumerate(mascotas): #animal es una tupla --> (indice , valor)
    indice = animal[0]
    mascota = animal[1]
    print(f"El indice del {mascota} en la lista de mascotas es {indice}")

#Usando el else (siempre se ejecuta luego del for)
for animal in mascotas:
    print(f"Tengo un {animal} de mascota")
else:
    print(f"Esas son todas mis mascotas el ultimo nombrado fue el {animal}")