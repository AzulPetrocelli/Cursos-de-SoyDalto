#Creo la clase Persona
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

#Creo la clase Estudiante
class Estudiante():
    #Redefino el constructor
    def __init__(self, notas, universidad):
        #Agrego atributos propios de la subclase estudiante
        self.notas = notas
        self.universidad = universidad
        
    def promedio_notas(self):
        promedio = sum(self.notas) / len(self.notas)
        return f"Mi promedio en la universidad es de {int(promedio)}"

#Creo la clase Empleado
class Empleado():
    #Redefino el constructor
    def __init__(self, trabajo, salario):
        #Agrego atributos propios de la subclase empleado
        self.trabajo = trabajo
        self.salario = salario
    
    def presentacion(self):
        return f"soy {self.trabajo}"

#Creamos una clase que hereda de las clases Persona, Estudiante y Empleado
class EstudianteEmpleado(Persona, Estudiante, Empleado):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad, trabajo, salario):
        #Defino el constructor con los de las clases heredadas
        Persona.__init__(self, nombre, edad, nacionalidad)
        Estudiante.__init__(self, notas, universidad)
        Empleado.__init__(self, trabajo, salario)
    
    #Defino un metodo utilizando los metodos de las clases heredadas    
    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} tengo {self.edad} años {super().presentacion()} estudio en la {self.universidad} {super().promedio_notas()}")

#Intancio la clase EstudianteEmpleado
estudiante_empleado_azul = EstudianteEmpleado("Azul", 22, "Argentino", [8,10, 4, 6], "UTN", "Desarrollador Web Full Stack", 750000)

#Llamo al metodo presentarse() de la clase EstudianteEmpleado
estudiante_empleado_azul.presentarse()

#Saber si una clase es subclase de otra clase
herencia = issubclass(EstudianteEmpleado, Persona)
print(herencia) #True
herencia = issubclass(EstudianteEmpleado, Estudiante) 
print(herencia) #True
herencia = issubclass(EstudianteEmpleado, Empleado) 
print(herencia) #True
herencia = issubclass(Estudiante, Empleado) 
print(herencia) #False

#Saber si un objeto es una instancia de una clase
instancia = isinstance(estudiante_empleado_azul, Persona)
print(instancia) #True
instancia = isinstance(estudiante_empleado_azul, Estudiante)
print(instancia) #True
instancia = isinstance(estudiante_empleado_azul, Empleado)
print(instancia) #True
instancia = isinstance(estudiante_empleado_azul, EstudianteEmpleado)
print(instancia) #True