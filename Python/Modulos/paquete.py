#Para que python reconosca una carpeta como paquete tiene
# que contener un modulo con el nombre __init__.py

import Paquete

#Tipo de dato de un paquete
print (type(Paquete))

#Direccion del paquete
print(Paquete.__path__)