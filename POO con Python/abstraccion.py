class Auto():
    def __init__(self):
        self._estado = "apagado"
        
    def encender(self):
        self._estado = "encendido"
        print("El auto esta encendido")
    
    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("Conduciendo el auto")
    
mi_auto = Auto()
mi_auto.conducir()

#Cuando el usuario llama al metodo conducir no piensa en la logica
# que hay detras, porque estamos abstrayendo su funcionamiento
# abstraccion: ocultar la complejidad interna de un sistema