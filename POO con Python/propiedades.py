class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        
    @property #Con esto le decimos a la clase que este metodo es un getter
    def get_nombre(self):
        return self.__nombre
    
    # Reutilizo, en realidad lo mas practico seria
    # poner algo generico en ambos como nombre, por polimorfismo
    @get_nombre.setter
    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre
    
    # Creamos un deleter para el nombre
    @get_nombre.deleter
    def delete_nombre(self):
        del self.__nombre
    
    # Forma idonea de hacerlo
    @property
    def edad(self):
        return self.__edad
    
    # El mismo nombre que en el property
    @edad.setter
    def edad(self, new_edad):
        self.__edad = new_edad
    
    # Creamos un deleter para la edad
    @edad.deleter
    def edad(self):
        del self.__edad
    
    
petro = Persona("Azul", 22)

#Usamos el setter para cambiar el nombre y la edad
petro.set_nombre = "Martin"
petro.edad = 23

#Usamos los getters, como lo definimos en la clase NO VAN LOS ()
print(petro.get_nombre)
print(petro.edad)

# Elimino los valores de sus atributos, si
# trato de mostrarlos me va a tirar error
del petro.delete_nombre
del petro.edad