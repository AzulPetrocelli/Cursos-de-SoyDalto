#Creo una clase con un constructor, la clase va sin ()
class Celular:
    #__init__ se ejecuta automaticamente cuando instancias la clase
    def __init__(self, nombre_marca, nombre_modelo, resolucion_camara):
        self.marca = nombre_marca
        self.modelo = nombre_modelo
        self.camara = resolucion_camara
    
    #Creamos los metodos de la clase celular(deben autoreferenciarse con self)
    def llamar(self):
        print(f"Estas haciendo un llamado desde un {self.marca} modelo {self.modelo}")
    
    def cortar(self):
        print(f"Cortaste la llamada desde tu {self.marca} modelo {self.modelo}")

#Creamos un objeto instanciando la clase y seteando los valores de sus atributos
celular = Celular("Samsung", "S23", "48MP")

#Llamo a los metodos del objeto
celular.llamar()
celular.cortar()