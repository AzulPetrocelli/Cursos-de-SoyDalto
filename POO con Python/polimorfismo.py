class Gato():
    def sonido(self):
        return "Miau"

class Perro():
    def sonido(self):
        return "Guau"
    
class Vaca():
    def sonido(self):
        return "Muuuu"
    
    
def hacer_sonido(animal):
    print(animal.sonido())
    
perro = Perro()
gato = Gato()

#Puedo usar el mismo metodo porque se llaman igual, solo se implementan de formas diferentes
hacer_sonido(perro)
hacer_sonido(gato)
