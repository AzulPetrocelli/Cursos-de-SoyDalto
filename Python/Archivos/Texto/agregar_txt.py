#Abrimos el archivo para agregar
with open("Python\\Archivos\\Texto\\texto.txt", "a", encoding="UTF-8") as archivo:
    
    #Usando bucle para agregar varias lineas con write (no sobreescribe el original)
    for i in range(5):
        archivo.write(f"\nLinea {i+1} agregada")