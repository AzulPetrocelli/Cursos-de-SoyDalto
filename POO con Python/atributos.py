#Creo una clase con un constructor, la clase va sin ()
class Celular:
    #__init__ se ejecuta automaticamente cuando instancias la clase
    def __init__(self, nombre_marca, nombre_modelo, resolucion_camara):
        self.marca = nombre_marca
        self.modelo = nombre_modelo
        self.camara = resolucion_camara

#Creamos un objeto instanciando la clase y seteando los valores de sus atributos
celular = Celular("Samsung", "S23", "48MP")

#Muestro los atributos del objeto
print(celular.marca)
print(celular.modelo)
print(celular.camara)