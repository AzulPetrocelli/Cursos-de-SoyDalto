from abc import ABC, abstractmethod

#Creamos una clase Abstracta 
class Persona(ABC):
    #Definimos un metodo abstracto
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
            
    @abstractmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print("Hola me llamo {self.nombre} y tengo {self.edad} años")

# Si hago esto me va a tirar error ya que no 
# podemos instanciar objetos con clases abstractas,
# solo podemos crear clases a traves de estas

#azul = Persona("Azul", 22, "Masculino", "Programacion")

#Creo una clase que hereda de la clase abstracta Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    #Implemento de otra forma el metodo que estaba en la clase abstracta   
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")

#Defino un objeto con la clase Estudiante que es una herencia
# de la clase abstracta, aca ya no me tira error
azul = Estudiante("Azul", 22, "Masculino", "Programacion")

azul.hacer_actividad()

#IMPORTANTE: Si una clase hereda de una clase abstracta, SI O SI
# tiene que tener definido TODOS los metodos abstractos que tiene
# , por mas que no los necesite la clase instanciada, en ese calo
# le ponemos pass de lo contrario nos va a tirar un error