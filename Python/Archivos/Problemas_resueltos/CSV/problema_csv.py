#Consigna: Cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("Python\\Archivos\\Problemas_resueltos\\CSV\\datos.csv")

#Convertir a string los datos de la columna edad
df["Edad"] = df["Edad"].astype(str)

#Mostrar el tipo de dato del primer elemento de la columna edad
#print(type(df["Edad"][0]))

#Remplazar apellido Petrocelli por Lopez
df["Apellido"].replace("Petrocelli", "Lopez", inplace=True)
#print(df["Apellido"])

#Eliminar filas con datos repetidos
df = df.drop_duplicates()
#print(df)

#Eliminar filas con datos faltantes
df = df.dropna()
#print(df)

#Creando un csv con el dataframe resultante (limpio)
df.to_csv("Python\\Archivos\\Problemas_resueltos\\CSV\\limpio.csv")