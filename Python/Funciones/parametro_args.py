#Utilizando el operador * como argumento(args) (se usa cuando la cant de parametros a
# recibir es indefinida, ponemos el asterisco en el ultimo parametro de la funcion)

def suma (nombre, *anios_estudiando):
    return f"{nombre} estudio en total {sum(anios_estudiando)} años"

print(suma("Azul", 6,7,3))