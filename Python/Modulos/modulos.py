#Importar el modulo "modulo_saludar" (sin la extencion .py)
import modulo_saludar #Es un objeto namespace

#Ahora la funcion saludar es un metodo
saludo = modulo_saludar.saludar("Azul")
print(saludo)

print(type(modulo_saludar)) # <class 'module'>

#Importae modulo y ponerle un nombre a un modulo
import modulo_saludar as m_saludar 

#Acceder al nombre real del modulo que importamos
print(m_saludar.__name__)

#Acceder al nombre real del modulo donde nos encontramos
print(__name__)

#Ahora la funcion saludar es un metodo con otro nombre
saludo = m_saludar.saludar("Azul")
print(saludo)

#Importar solo una funcion del modulo 
from modulo_saludar import saludar
saludo = saludar("Azul")
print(saludo)

#Importar solo una funcion y cambiarle el nombre
from modulo_saludar import saludar as saludoA
saludo = saludoA("Azul")
print(saludo)

#Importar dos funciones
from modulo_saludar import saludar, saludo_raro
saludo1 = saludar("Azul")
saludo2 = saludo_raro("Azul")
print(saludo1)
print(saludo2)

#importar dos funciones y cambiarles el nombre
from modulo_saludar import saludar as normal, saludo_raro as raro
saludo1 = normal("Azul")
saludo2 = raro("Azul")
print(saludo1)
print(saludo2)

#Importar todo de un modulo
from modulo_saludar import * #MALA PRACTICA, PORQUE LOS MODULOS SON EXTENSOS
saludo1 = saludar("Azul")
saludo2 = saludo_raro("Azul")
print(saludo1)
print(saludo2)

#IMPORTANTE: PUEDEN HABER VARIABLES CON EL MISMO NOMBRE DE UNA FUNCION IMPORTANDOLA
# EN SU LUGAR, LO RECOMENDABLE ES QUE LAS FUNCIONES COMIENCEN CON MAYUSCULA
