#Dos listas, una con nombres otra con apellidos
nombres = ["Lucas", "Matias", "Camila", "Pedro", "Roberto"]
apellidos = ["Dalto", "Zing", "Olmos", "Petroceli", "Totototo"]

#Registrar esta informacion en un txt de forma optima

with open("Python\\Archivos\\Problemas_resueltos\\TXT\\nombres_y_apellidos.txt", "w", encoding="UTF-8") as archivo:
    archivo.writelines("Los datos son:\n\n")
    
    #for nombre,apellido in zip(nombres,apellidos):
    #   archivo.writelines(f"Nombre: {nombre},  Apellido: {apellido} \n")
        
    #alternativa de Dalto en una sola linea (IMPORTANTE: debe estar entre [])
    [archivo.writelines(f"Nombre: {n},  Apellido: {a} \n-----------------\n") for n,a in zip(nombres,apellidos)]
