import os

# Muestra la carpeta desde la que Python está ejecutando el script
print(os.getcwd()) # C:\Users\azulp\Desktop\Mis Cosas\Cursos de SoyDalto

#Abrimos el archivo y lo guardamos en una variable
archivo = open("Python\\Archivos\\Texto\\texto.txt", encoding="UTF-8")
#Nota: el UTF-8 es para que reconosca los caracteres especiales del texto como las comas

#Leer archivo completo
archivo_leido = archivo.read()
print(archivo_leido)

#Leer linea por linea y guardarla en una lista
#lineas = archivo.readlines()
#print(lineas)

#Leemos la primera linea
#linea1 = archivo.readline()
#print(linea1)

#Leemos los primeros 20 caracteres de la primer linea
#caracteres20 = archivo.readline()
#print(caracteres20)

#Cerrar el archivo
archivo.close()

#IMPORTANTE: una vez que el archivo se lee no se puede volver a leerse si no lo
# cerramos antes, por motivos de seguridad, por eso el codigo esta comentado.