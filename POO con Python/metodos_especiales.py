class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    #Define como mostrarse en pantalla en un print, 
    # representacion informal, legible para el usuario
    def __str__(self):
        return f'Persona(nombre={self.nombre}, edad= {self.edad})'
    
    #Define como se representara un objeto, representacion 
    # formal, util para debuggin, ATENTO A LAS ""
    def __repr__(self):
        return f'Persona("{self.nombre}", "{self.edad}")'
        
    #SOBRECARGA DE OPERADORES: Definimos que va a pasar cuando 
    # SE SUMEN DOS O MAS OBJETOS con la funcion __add__()
    def __add__(self, otro_objeto):
        nuevo_valor = self.edad + otro_objeto.edad
        return Persona(self.nombre + otro_objeto.nombre ,nuevo_valor)

azul= Persona("Azul", 22)
lucas= Persona("Lucas", 23)
matias= Persona("Matias", 46)

#Muestro el objeto por pantalla y me muestra lo que defini en __str__
#print(azul)

#Guardo la representacion del objeto
#repr(azul) == 'Persona("{self.nombre}", "{self.edad}")'
representacion = repr(azul)

#Ejecuta la representacion del objeto, tiene que estar en un string.
resultado = eval(representacion)

#Muestro su representacion
print(resultado)

nueva_persona = azul + matias + lucas

#Existen varias funciones de sobrecargas de operadores ademas de __add__()

#Sobrecarga de operadores aritmeticos
#__add__(self, other): para el operador de suma (+).
#__sub__(self, other): para el operador de resta (-).
#__mul__(self, other): para el operador de multiplicación (*).
#__div__(self, other): para el operador de división (/). (Nota: en Python 3 se usa __truediv__ en lugar de __div__)
#__mod__(self, other): para el operador de módulo (%).
#__pow__(self, other): para el operador de exponenciación (**).

#----------------------------------------------------------------------------

#Sobrecarga de operadores de Comparación:

#__eq__(self, other): para el operador de igualdad (==).
#__ne__(self, other): para el operador de desigualdad (!=).
#__lt__(self, other): para el operador menor que (<).
#__gt__(self, other): para el operador mayor que (>).
#__le__(self, other): para el operador menor o igual que (<=).
#__ge__(self, other): para el operador mayor o igual que (>=).

#----------------------------------------------------------------------------

#Sobrecarga de operadores de Asignación:

#__iadd__(self, other): para el operador de suma en asignación (+=).
#__isub__(self, other): para el operador de resta en asignación (-=).
#__imul__(self, other): para el operador de multiplicación en asignación (*=).
#__idiv__(self, other): para el operador de división en asignación (/=). (Nota: en Python 3 se usa __itruediv__)
#__imod__(self, other): para el operador de módulo en asignación (%=).
#__ipow__(self, other): para el operador de exponenciación en asignación (**=).

#----------------------------------------------------------------------------

#Otros:

#__str__(self): Sobrecarga del operador str(). Devuelve una representación legible como cadena del objeto.
#__len__(self): Sobrecarga del operador len(). Devuelve la longitud del objeto.
#__getitem__(self, index): Sobrecarga del operador de indexación ([]). Permite acceder a elementos del objeto por índice.





























