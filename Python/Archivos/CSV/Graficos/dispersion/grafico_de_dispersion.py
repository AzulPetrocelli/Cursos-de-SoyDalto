import pandas as pd
#Libreria de visualizacion de datos --> py -m pip install matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Python\\Archivos\\CSV\\Graficos\\dispersion\\dispersion.csv")

#Creando el grafico
sns.scatterplot(x="tiempo", y="dinero", data = df)

#mostrando el grafico
plt.show()