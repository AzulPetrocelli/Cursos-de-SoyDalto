class MiClase:
    def __init__(self):
        #Creamos un atributo "privado", debe arrancar con _
        self._atributo_privado = "Valor privado"
        #Creamos un atributo realmente privado, debe arrancar con __
        self.__atributo_muy_privado = "Valor muy privado"
        
        
objeto = MiClase()

#Accediendo al atributo "privado"
print(objeto._atributo_privado)

#Intentando acceder al atributo privado, me tira un error
# Solo se pueden obtener atributos privados a traves de getters
#print(objeto.__atributo_muy_privado)