#Creando una lista (se puede modificar)
lista = ["Azul", True, 1.85]

#Mostrando el primer elemento
print(lista[0]) #"Azul"

#Creando una tupla (no se puede modificar)
tupla = ("Azul", True, 1.85)

#Mostrando el primer elemento
print(tupla[0]) #"Azul"

#Creando un conjunto (set) (no se accede a elementos por indice, no almacena datos duplicados)
conjunto = {"Azul", True, 1.85}

#Creando un diccionario (dict) (La estructura es key : value y separamos por comas salvo el ultimo)
diccionario = {
    'nombre': "Azul",
    'apellido': "Petrocelli",
    'edad': 22,
    'altura': 1.85,
    'estudiando': True
}

print(diccionario['edad'])