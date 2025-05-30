# DIP: Depency inversion Principle

#Este principio dicta que los módulos de alto nivel no deben 
# depender de módulos de bajo nivel. Ambos deben depender de
# abstracciones.
#Las abstracciones no deben depender de los detalles. Los detalles
# deben depender de las abstracciones.

#Dicho de otra forma 

# EJEMPLO DE VIOLACION DE DIP-----------------------------------------------------

class Diccionario1:
    def verificar_palabta(self, palabra):
        #Logica interna para verificar palabras
        pass

class CorrectorOrtografico:
    def __init__(self):
        self.diccionario = Diccionario1() # --> el problema es que el corrector depende del diccionario
    
    def corregir_texto(self, texto):
        #Usamos el diccionario para corregir el texto
        pass

# EJEMPLO DE IMPLEMENTACION DE DIP-----------------------------------------------------

# Tenemos un Modulo de alto nivel que toma decisiones importantes
# (Corrector) y un Modulo de bajo nivel que hace tareas concretas
# (Diccionario).
# En lugar de que el módulo de alto nivel dependa directamente del 
# módulo de bajo nivel, ambos deben depender de una interfaz o 
# clase abstracta común.

from abc import ABC, abstractmethod

#Clase base
class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass

#Subclase
class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #logica para verificar palabras SI ESTA EN EL DICCIONARIO
        pass

class CorrectorOrtografico:
    def __init__(self, verificador):
        #Ya no depende de una clase sino de una abstraccion del 
        # VerificadorOrtografico  lo hace mas flexible y escalable
        # ya que ahora no depende directamente de la clase Diccionario()
        self.verificador = verificador 
        
    def corregir_texto(self, texto):
        #Usamos el verificador para corregir texto
        pass
    
#Podriamos crear mas clases que funcionen como verificadores y crear 
# un corrector ortografico para estas

class ServicioOnline(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #Logica para verificar palabra desde el servicio web
        pass
    
#Podemos crear un corrector con un Diccionario como verificador
corrector = CorrectorOrtografico(Diccionario())

#Tambien podemos crear un corrector con un Servicio Online como verificador
corrector = CorrectorOrtografico(ServicioOnline())