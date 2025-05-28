#Importamos el modulo "re" de la biblioteca estandar 
# de Python para trabajar con expreciones regulares
import re

texto = '''Hola azul, espero que estes disfrutando
del curso de Python. Vas a avanzar en tu trabajo 
muy rapido, exitos Azul vas a ser el numero 1.
Esta es la liena 4 de texto.
Esta es la liena 5 de texto.
TE AMO 3000
abababab abbbb aa ab ba bb
Hola al nuevo mundo'''

#Me devuelve la primer coincidencia
#primer_coincidencia = re.search("Hola", texto)
#print(primer_coincidencia)

#Me devuelve todas las coincidencias
todas_las_coincidencias_con_distincion = re.findall("que", texto)
#print(todas_las_coincidencias_con_distincion)

#Deja de distinguir entre mayusculas y minusculas
todas_las_coincidencias_sin_distincion = re.findall("azul", texto, flags= re.IGNORECASE)
#print(todas_las_coincidencias_sin_distincion)

#Formato de expresiones regulares --> r"expresion"

#\d --> busca digitos numericos del 0 al 9
resultado = re.findall(r"\d", texto)
#print(resultado)

#\D --> busca TODO MENOS digitos numericos
resultado = re.findall(r"\D", texto)
#print(resultado)

#w --> busca caracteres alfanumericos es decir de [a-z A-Z 0-9 _]
resultado = re.findall(r"\w", texto)
#print(resultado)

#W --> busca TODO MENOS caracteres alfanumericos
resultado = re.findall(r"\W", texto)
#print(resultado)

#\s -> busca espacios en blanco -> espacios, tabs, saltos de linea
resultado = re.findall(r"\s", texto)
#print(resultado)

#\S -> busca TODO MENOS espacios en blanco
resultado = re.findall(r"\S", texto)
#print(resultado)

# . --> busca saltos de linea
resultado = re.findall(r"\n", texto)
#print(resultado)

#. --> busca TODO MENOS saltos de linea
resultado = re.findall(r".", texto)
#print(resultado)

#\ --> cancelar caracteres especiales, cancelando la funcion del punto y buscando puntos
resultado = re.findall(r"\.", texto)
#print(resultado)

#Armando una expresion que busque un numero, seguido de un punto seguido de un espacio
resultado = re.findall(r'\d\.\s', texto)
#print(resultado)

#^ --> Busca el comienzo de cada linea, buscando Esta al principio de la linea
# flags=re.M activa la multilinea
resultado = re.findall(r'^Esta', texto, flags=re.M)
#print(resultado)

#$ --> Busca el final de la linea
resultado = re.findall(r'texto.$', texto, flags=re.M)
#print(resultado)

#{n} --> Busca n cantidad de veces el valor de la izquierda
resultado = re.findall(r'\d{4}', texto, flags=re.M) #buscando 4 digitos consecutivos
#print(resultado)

#{n, m} --> Busca de n a m cantidad de veces el valor de la izquierda
resultado = re.findall(r'\d{1,4}', texto, flags=re.M) #buscando de 1 a 4 digitos consecutivos
#print(resultado)

#devolver todas las posibles combinaciones de a y b --> aa, bb, ab, ba
resultado = re.findall(r'[ab]{2}', texto, flags=re.M) 
#print(resultado)

#devolver de 1 a 4 todas las ab
resultado = re.findall(r'(ab){1,4}', texto, flags=re.M) 
#print(resultado)

#devolver todas las a seguido de 1 a 4 b
resultado = re.findall(r'ab{1,4}', texto, flags=re.M) 
#print(resultado)

# | --> Busca una cosa O otra cosa
resultado = re.findall(r'ab{1,4}|Hola', texto, flags=re.M) 
#print(resultado)

# * busca 0 o mas ocurrencias de lo que esta a la izquierda
resultado = re.findall(r'Hola.*', texto, flags=re.M) 
#print(resultado)

# + busca 1 o mas ocurrencias de lo que esta a la izquierda
resultado = re.findall(r'Hola.+', texto, flags=re.M) 
#print(resultado)

#? busca 0 o 1 ocurrencia de lo de la izquierda, si hay mas de 1 no me lo muestra, es opcional
new_text = re.findall("a?", texto, flags=re.M)
print(new_text)

#Reemplazar en el texto con sub(), reemplazamos las vocales por *
new_text = re.sub("[aeiou]", "*", texto)
#print(new_text)