#Accedemos a un modulo en la carpeta Funciones_buenas
import Funciones_buenas.saludar

print(Funciones_buenas.saludar.saludar("Azul"))

#Accedemos a un modulo en la carpeta Funciones_buenas y le cambiamos el nombre
import Funciones_buenas.saludar as m_saludar

print(m_saludar.saludar("Azul"))

#Si quisieramos acceder a Funciones_buenas2 que esta una carpeta atras usamos el modulo sys

import sys

#Mostrar tupla con todos los modulos que estan en sys
print(sys.builtin_module_names)

#Muestra una lista con la ruta del archivo y las rutas de los modulos de python
print(sys.path)

#Agregamos la direccion de Funciones_buenas2 al final de sys
sys.path.append("C:\\Users\\azulp\\Desktop\\Mis Cosas\\Cursos de SoyDalto\\Python\\Funciones_buenas2")

import saludar2 as m_saludar

saludo = m_saludar.saludo_raro("Azul")
print(saludo)

#IMPORTANTE: python le da mayor prioridad a los modulos nativos