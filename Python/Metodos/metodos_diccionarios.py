diccionario = {
    'nombre' : 'Azul',
    'apellido' : 'Petrocelli',
    'edad' : 22
}

#Retornar lista de claves (keys) (tambien nos siver para iterar)
claves = diccionario.keys()

#Devolver el valor de una clave, si retorna "none" significa que no tiene valor o no existe la clave
valor_nombre = diccionario.get('nombre')
valor_apellido = diccionario.get('apellido')

#Eliminar un elemento/s del diccionario
diccionario.pop('edad', 'apellido')

#Retornar lista de tuplas ("clave", "valor") por cada elemento del diccionario
diccionario_iterable = diccionario.items()

#Eliminar todos los elementos de la lista
diccionario.clear()