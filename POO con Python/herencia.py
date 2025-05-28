#Creo una clase padre
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

#Creo una subclase de Persona
class Empleado(Persona):
    #Redefino el constructor
    def _init_(self, nombre, edad, nacionalidad, trabajo, salario):
        #Heredo los atributos del metodo __init()__ de la clase padre
        super().__init__(self,nombre, edad, nacionalidad)
        #Agrego atributos propios de la subclase empleado
        self.trabajo = trabajo
        self.salario = salario


class Estudiante(Persona):
        #Redefino el constructor
    def _init_(self, nombre, edad, nacionalidad, notas, universidad):
        #Heredo los atributos del metodo __init()__ de la clase padre
        super().__init__(self,nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad

empleado_azul = Empleado("Azul", 22, "Argentino", "Desarrollador Web Full Stack", 750000)
estudiante_azul = Estudiante("Azul", 22, "Argentino", [8,10, 4, 6], "UTN")
