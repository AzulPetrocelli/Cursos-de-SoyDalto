# LSP: Liskov's Substitution Principle

# Se requiere cuando las clases derivadas(subclases) 
# tienen que se sustituibles por sus clases base,
# es decir los atributos y metodos de la clase base
# deben poder utilizarse por podas las subclases derivadas 
# Si yo creo una clase base, no puede haber una subclase
# que no aplique sus metodos o no los sobreescriba.

class Avesita:
    def volar(self):
        print("Estoy volando")
        
class Pinguinito(Avesita):
    def volar(self):
        pass #Los pinguinos no vuelan

#Esto es justamente un problema que se resuelve usando el
# Metodo de sustitucion de Liskov's
# Ya que la subclase no puede hacer algo que la clase base si

# Para esto tenemos que crear otra clase Ave y crear dos
# Subclases para recategorizarlos

class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        print("Estoy volando")
        
class AveNoVoladora(Ave):
    pass

class AveNadadora(Ave):
    pass

# Ya categorizadas, en la clase base Ave van a ir todas las 
# caracteristicas en comun que tengan las aves que vuelan y
# que no vuelan y las que nadan