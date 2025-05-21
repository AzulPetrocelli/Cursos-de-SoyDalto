#MI RESOLUCION----------------------------------------------------------------
#Ingresar alumnos a la lista hasta que no complete el campo nombres y mostrarla al final
def ingresar_datos_alumno():
    lista_de_alumnos = []
    
    while True:
        nombre = input("Ingrese el nombre del compañero (Enter para salir): ")
        if nombre == "":                                                        #Si no ingreso un valor corta
            break
        
        edad = input("Ingrese la edad del compañero: ")
        lista_de_alumnos = ingresar_alumno_ordenadamente(lista_de_alumnos, nombre, int(edad))
        
    # Mostrar la lista ordenada al final
    print("\nLista de compañeros ordenada por edad:")
    for nombre, edad in lista_de_alumnos:
        print(f"{nombre} - {edad} años")
    
    return lista_de_alumnos

#Ingresar a los alumnos en la lista de menor a mayor edad
def ingresar_alumno_ordenadamente(lista, nombre, edad):
    for indice,alumno in enumerate(lista):                  #Convierto las tuplas de la lista (indice, (nombre, edad)) y la descompongo
        if alumno[1] > edad :                               #Comparo la edad del alumno dada con la del alumno actual
            lista.insert(indice, (nombre, edad))            #Inserto una tupla alumno en el indice indice
            return lista
    
    # Si no se insertó en ningún lugar, agregar al final
    lista.append((nombre, edad))
    return lista

#Retornar asistente del profesor
def asistente_del_curso (lista):
    asistente = lista[0][0]
    print(f"El asistente es {asistente}")
    return asistente

#Retornar profesor de la clase
def profesor_del_curso (lista):
    profesor = lista[-1][0]
    print(f"El profesor es {profesor}")
    return profesor

#Llamo a las funciones
lista_de_alumnos =ingresar_datos_alumno()
asistente_del_curso(lista_de_alumnos)
profesor_del_curso(lista_de_alumnos)

#SOLUCION DALTO----------------------------------------------------------------
#falto el profe y los pibes van a armar la clase.

#funciòn para obtener al asistente y al profesor segun la edad.
def obtener_compañeros(cantidad_de_compañeros):
    
    #creando la lista con los compañeros
    compañeros = []
    
    #ejecutando un for para pedir informaciòn de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input("ingrese el nombre del compañero: ")
        edad = int(input("ingrese la edad del compañero: "))
        compañero = (nombre,edad)
        
        #agregando la informaciòn a la lista
        compañeros.append(compañero)
        
    #ordenandolos de menor a mayor segùn su edad    
    compañeros.sort(key=lambda x:x[1]) #sort recorre la lista, x es un compañero de la lista en un instante
    
    #compañeros[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre
    #para definir al asistente y al profesor.
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    #retornamos una tupla
    return asistente,profesor

#desempaquetamos lo que nos retorna la funciòn
asistente,profesor = obtener_compañeros(5)

#mostrando el resultado
print(f"El profesor es: {profesor} y su asistente es {asistente}")