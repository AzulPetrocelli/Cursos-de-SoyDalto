#Definir una funcion simple
def saludar():
    print("Hola mundo!")
    
#Ejecutar mi funcion
saludar()

#Crear una funcion con parametros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo=="hombre"):
        adjetivo = "rey"
    else:
        adjetivo = "reine"
    
    print(f"Hola {nombre} mi {adjetivo} ¿Como andas?")
    
#ejecutando mi funcion com parametros
saludar("Azul", "Hombre")
saludar("Azul", "Mujer")
saludar("Azul", "No binario")

#Crear una funcion que retorne valores
def crear_contraseña_random(numero):
    chars = "abcdefghij"
    num = str(numero)#paso el num a string
    num = int(num[0])#tomo el primer caracter
    c1 = num -1
    c2 = num
    c3 = num -3
    password = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return password,numero #retornamos una tupa

#Desempaquetando la funcion
contraseña,num = crear_contraseña_random(98)

#Mostrando los resultados obtenidos y los datos usados
print(f"Tu contraseña random creada a partir del {num} es: {contraseña}")
