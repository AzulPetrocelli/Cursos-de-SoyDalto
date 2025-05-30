# ISP: Interfase segregation principle

# este principio nos dice que el cliente no debe
# ser forzado a depender de interfases que no utilice
# por ejemplo una clase base Trabajador() con los metodos
# comer(), dormir(), trabajar(), lo uso para crear dos
# subclases Humano() y Robot(), ambos heredan los metodos 
# de la clase base, pero los Robots no comen ni duermen
# osea que no voy a usar esos metodos, pero aun asi dependo
# de ellos ya que los herede de la clase base

from abc import ABC, abstractmethod

# FORMA INCORRECTA----------------------------------------------------------------------------------

class Trabajadorsito(ABC):
    @abstractmethod
    def comer(self):
        pass
    
    @abstractmethod
    def dormir(self):
        pass
    
    @abstractmethod
    def trabajar(self):
        pass

class Personita(Trabajadorsito):
    def comer(self):
        print("El trabajador esta comiendo")
    
    def dormir(self):
        print("El trabajador esta durmiendo")
    
    def trabajar(self):
        print("El trabajador esta trabajando")

class Robotito(Trabajadorsito):
    def trabajar(self):
        print("El robot esta trabajando")
    
    #No los voy a usar pero dependo de ellos
    # porque sino el programa no funciona
    # es decir dependo de una interfas que no uso
    def comer(self):
        pass
    
    def dormir(self):
        pass
    
    
# FORMA DE SOLUCIONARLO----------------------------------------------------------------------------------

#Divido las funcionalidades
class Trabajador(ABC):
    
    @abstractmethod
    def trabajar(self):
        pass

class Comedor(ABC):
    
    @abstractmethod
    def comer(self):
        pass
    
class Dormilon(ABC):
    
    @abstractmethod
    def dormir(self):
        pass
    
# Heredo de las clases las funcionalidades que necesita
class Persona(Trabajador, Comedor, Dormilon):
    def comer(self):
        print("El trabajador esta comiendo")
    
    def dormir(self):
        print("El trabajador esta durmiendo")
    
    def trabajar(self):
        print("El trabajador esta trabajando")


#Robot ya no depende de comer() y dormir()
class Robot(Trabajador):
    def trabajar(self):
        print("El robot esta trabajando")