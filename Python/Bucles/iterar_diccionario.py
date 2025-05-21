diccionario = {
    "nombre": "Azul",
    "apellido": "Petrocelli",
    "edad": 22
}

#Mostrar claves del diccionario
for clave in diccionario:
    print(clave)
    
#Mostrar clave valor del diccionario en forma de tupla
for clave_valor in diccionario.items():
    print(clave_valor) #--> (clave, valor)
    
#Recorrer y seleccionar clave y valor
for clave_valor in diccionario.items():
    key = clave_valor[0]
    value = clave_valor[1]
    print(f"La clave es: {key} y el valor es: {value}")