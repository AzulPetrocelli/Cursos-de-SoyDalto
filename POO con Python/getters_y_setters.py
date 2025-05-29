class Persona:
    def __init__(self,nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    #Creamos el getter para nombre
    def get_nombre(self):
        return self.__nombre
    
    #Creamos el setter para nombre
    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre
    
    #Creamos el getter para edad
    def get_edad(self):
        return self.__edad
    
    #Creamos el setter para edad
    def set_edad(self, new_edad):
        self.__edad = new_edad

azul = Persona("Azul", 22)

#Cambiando los atributos con el setter
azul.set_nombre("Blue")
azul.set_edad(25)

#Mostrando los atributos a traves de los getters
print(azul.get_nombre())
print(azul.get_edad())