import pandas as pd
#Libreria de visualizacion de datos --> py -m pip install matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Python\\Archivos\\CSV\\Graficos\\lineal\\pedos.csv")

#Creando el grafico
sns.lineplot(x="fecha", y="pedos", data = df)

#Agregando un punto en el grafico
plt.plot("01-09", 17, "o")

#Mostrando el grafico
plt.show()