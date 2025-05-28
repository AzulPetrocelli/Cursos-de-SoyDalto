#Creo una clase
class Celular():
    #Atributos estaticos (Igual para todas las instancias)
    marca = "Samsung"
    modelo = "S23" 
    camara = "48MP"

#Creo el objeto instanciando la clase
celular1 = Celular()

#Muestro los atributos del objeto
print(celular1.marca)
print(celular1.modelo)
print(celular1.camara)