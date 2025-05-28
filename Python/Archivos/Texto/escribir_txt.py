with open("Python\\Archivos\\Texto\\texto.txt", "w", encoding="UTF-8") as archivo:
    #Sobreescribiendo el archivo
    #archivo.write("Acabo de sobreescribir el archivo")
    
    #Agregando dos lineas con writelines (sobreescribe el original)
    archivo.writelines(["- Hola maestro como andas?", " Todo bien?\n"])
    archivo.writelines(["- Que onda maquina,", " todo bien y vos?\n"])
    