#Un decorador es una funcion que recibe otra funcion
# como parametro, retornando una funcion modificada
# agregandole funciones antes y/o despues a la funcion
# que pasamos como parametro

#Defino el decorador
def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la funcion")
        funcion()
        print("Despues de llamar a la funcion")
    return funcion_modificada

#Defino una funcion que quiero decorar
# def saludo():
#     print("Hola Azul")

# #Creamos la funcion decorada
# saludo_modificado = decorador(saludo)

# #Llamamos a la funcion decorada
# saludo_modificado()

#Forma mas optima de crear una funcion decorada
@decorador
def saludo():
    print("Hola Azul")

saludo()
