import pandas as pd
#Libreria de visualizacion de datos --> py -m pip install matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Python\\Archivos\\CSV\\Graficos\\bigotes\\bigotes.csv")

#Creando el grafico
sns.boxplot(x="categoria", y="valor", data = df)

#mostrando el grafico
plt.show()