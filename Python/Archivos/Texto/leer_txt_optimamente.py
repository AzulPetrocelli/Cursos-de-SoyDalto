#Abrimos el archivo con with open (Por defecto se abre en modo lectura)
with open("Python\\Archivos\\Texto\\texto.txt", "r", encoding="UTF-8") as archivo:
    #Leer archivo completo
    contenido = archivo.read()
    
    #Mostramos el archivo
    print(contenido)
    
    #No es necesario cerrarlo cuando usamos with open 