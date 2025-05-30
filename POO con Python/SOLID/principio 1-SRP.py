#SRP : Single Responsability Principle

#Cada clase debe tener una funcionalidad UNICA si llega
# a hacer dos cosas tenemos que separar esa clase y 
# que cada una tenga una funcionalidad diferente


#Esto es un ejemplo de lo que no se debe hacer, ya que la 
# clase auto se encarga de el combustible y de mover el auto

class ClaseAutoMala():
    def __init__(self):
        self.posicion = 0
        self.combustible = 100
    
    def mover(self, distancia):
        if self.combustible >= distancia / 2:
            self.posicion += distancia
            self.combustible -= distancia / 2
        else:
            print("No hay suficiente combustible")
    
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
    
    def obtener_combustible(self):
        return self.combustible
    
#Lo que debemos hacer es dividir la funcionalidad en distintas clases

class Auto():
    #Tanque es el objeto que vamos a crear de la clase TanqueDeCombustible
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque
        
    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print("Has movido el auto exitosamente")
        else:
            print("No hay suficiente combustible")
    
    def obtener_posicion(self):
        return self.posicion

class TanqueDeCombustible():
    def __init__(self):
        self.combustible = 100

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad

    def usar_combustible(self, cantidad):
        self.combustible -= cantidad
    
    def obtener_combustible(self):
        return self.combustible
    
#Creamos un objeto con estas clase
tanque = TanqueDeCombustible()
auto = Auto(tanque)

#Movemos el auto
print(auto.obtener_posicion())
auto.mover(10)
print(auto.obtener_posicion())
auto.mover(20)
print(auto.obtener_posicion())
auto.mover(60)
print(auto.obtener_posicion())
auto.mover(100)
print(auto.obtener_posicion())
auto.mover(100)
print(auto.obtener_posicion())