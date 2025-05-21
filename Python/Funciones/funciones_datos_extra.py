#Defino funcion frase con tres parametros
def frase(nombre, apellido, adjetivo):
    return f"Hola {nombre} {apellido}, sos {adjetivo}"

#Respetando el orden de los parametros
frase_resultante = frase("Azul", "Petrocelli", "La cabra")
print(frase_resultante)

#Forzar los argumentos (se debe hacer con todos los argumentos)
frase_resultante = frase(apellido = "Petrocelli",adjetivo = "La cabra", nombre = "Azul")
print(frase_resultante)


#Defino la misma funcion frase con un parametro OPCIONAL
def frase(nombre, apellido, adjetivo = "El GOAT"):
    return f"Hola {nombre} {apellido}, sos {adjetivo}"

#Cambio el parametro opcional
frase_resultante = frase("Azul", "Petrocelli", adjetivo = "La Cabra")
print(frase_resultante)

frase_resultante = frase("Azul", "Petrocelli", "La Cabra")
print(frase_resultante)

#Dejo el parametro opcional
frase_resultante = frase("Azul", "Petrocelli")
print(frase_resultante)