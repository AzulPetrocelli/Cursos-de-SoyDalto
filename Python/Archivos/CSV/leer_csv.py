#Importamos el modulo csv
import csv

with open("Python\\Archivos\\CSV\\datos.csv", "r", encoding="UTF-8") as archivo:
    reader = csv.reader(archivo)
    
    for fila in reader:
        print(fila)