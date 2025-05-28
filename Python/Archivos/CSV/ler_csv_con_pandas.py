#Nota: Tenemos que instalar el modulo de pandas para usarlo
# 1 Ejecutamos cmd como administrador
# 2 Instalamos pip --> py -m ensurepip --upgrade (verificar que lo tenemos instalado: py -m pip)
# 3 Instalamos pandas --> py -m pip install pandas

import pandas as pd
ruta = "Python\\Archivos\\CSV\\datos.csv"

#Guardamos el data frame (se compone por filas y columnas)
df = pd.read_csv(ruta)
#print(df1)

#Guardamos el data frame, aclarandole que sus columnas seran Name, Last name y Age
df = pd.read_csv(ruta, names=["Name", "Lastname", "Age"])
#print(df)

#Obteniendo los datos de la columna Name
nombres = df["Name"]
#print(nombres)

#Tecnica slicing
cadena = "0123456789"
#print(cadena[3:7]) #3456 no toma el 7
#print(cadena[:7]) #0123456
#print(cadena[3:]) #3456789 toma del 3 hasta el ultimo


#Ordenando data frame por la edad (por defecto es acendente)
df_ordenado_acendente = df.sort_values("Age")
#print(df_ordenado_acendente)

#Ordenando data frame por la edad de forma decendente
df_ordenado_decendente = df.sort_values("Age", ascending=False)
#print(df_ordenado_decendente)

#Concatenando los dos data frame
df1 = pd.read_csv(ruta)
df2 = pd.read_csv(ruta)

df_concatenado = pd.concat([df1, df2])
#print(df_concatenado)

#Accediendo al encabezado con head()
encabezado = df.head(0)
#print(encabezado)

#Accediendo al la primer fila con head()
primer_fila = df.head(1)
#print(primer_fila)

#Accediendo a las primeras 3 filas con head()
primeras_tres_filas = df.head(1)
#print(primeras_tres_filas)

#Accediendo a las ultimas 3 filas con tail()
ultimas_tres_filas = df.tail(3)
#print(ultimas_tres_filas)

#Accediendo a la cantidad de filas y columnas totales
filas_y_columnas_totales = df.shape
#print(filas_y_columnas_totales) # devuelve una tupla (cant.filas , cant.columnas)

#Obteniendo data estadistica del data frame
df_info = df.describe()
#print(df_info)

df_info = df1.describe()
#print(df_info)

#Accediendo a un elemento especifico del data freame con loc()
elemeto_especifico_loc = df.loc[3,"Age"]
#print(elemeto_especifico_loc)

#Accediendo a un elemento especifico del data freame con iloc()
elemeto_especifico_loc = df.iloc[3,2]
#print(elemeto_especifico_loc)

#Accediendo a todas las filas de una columna
apellidos = df.iloc[:,1]
#print(apellidos)

#Accediendo a la fila 3 con iloc
fila_3 = df.iloc[2,:]
#print(fila_3)

#Accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]
#print(fila_3)

#Accediendo a filas cuya edad es mayor a 30
mayor_que_30 = df1.loc[df1["Edad"]>30,:]
print(mayor_que_30)