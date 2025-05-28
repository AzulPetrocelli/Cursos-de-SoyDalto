import pandas as pd
#Libreria de visualizacion de datos --> py -m pip install matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Python\\Archivos\\CSV\\Graficos\\barras\\cofla_ingresos.csv")

#Creando el grafico
sns.barplot(x="fuente", y="ingresos", data = df)

#Obteniendo el todal de ingresoso
total_ingresos = df["ingresos"].sum()

#Mostrando el total de ingresos
print(f"El total de ingresos es de {total_ingresos} USD")

#mostrando el grafico
plt.show()


