'''
César Pardo - 23-marzo-2020
Código reutilizable, sólo agradecer :D
'''

import matplotlib.pyplot as plt
import numpy as np
import datetime
import plotly.graph_objects as go

x1 = np.linspace(0.0, 50, 100, 4000)

#Incluyo algunos datos para la comparación con el total del mundial, China e Italia
#y1 = lista_casos_Mundo = [87024,89068,90663]
#y2 = lista_casos_China = [79929,80134,80261]
#y3 = lista_casos_Italia = [1128,1689,1835,2502,3089,3858,4636]
y4 = lista_casos_Colombia 	= [0, 0, 0, 0, 0, 0, 1, 0, 0, 3, 0, 9, 0, 16, 35, 45, 57, 65, 102, 128, 158, 210, 235]
y5 = lista_casos_Brasil 	= [2, 2, 0, 0, 3, 8, 13,13,25,0,34,52,77, 98, 121,200,234,291,428, 621, 904, 1128,1546]
y6 = lista_casos_Ecuador 	= [1, 6, 7, 0, 10,13, 0, 0,14,15,17,0, 0, 23, 28,  37, 58,111,168,199, 426, 532, 789]
y7 = lista_casos_Venezuela 	= [0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0,0, 0,  0, 10,  15, 33, 33, 33, 33,  36,  36,  36]
y8 = lista_casos_Peru 	= [0, 0, 0, 0, 0, 0, 0, 1, 7, 9, 11, 17,22, 38,  43, 71,  86, 117, 145, 234, 263,  318,  363]
y9 = lista_casos_Chile 	= [0, 0, 0, 1, 3, 4, 5, 0, 10, 13, 17, 23,33, 43,  61, 75,  156, 201, 238, 342, 434,  537,  632]

fig, ax = plt.subplots(figsize=(5, 3), tight_layout=True)

#Se establece la fecha inicio para graficar los datos.
base = datetime.date(2020, 3, 1) 
#Se establece un rango del número de días que se quieran cargar y se encuentren en las listas.
time = [base + datetime.timedelta(days=x) for x in range(23)]

plt.xlabel("Fecha")# Inserta el título del eje X 
plt.ylabel("Cantidad total de personas reportadas")   # Inserta el título del eje X 
plt.title("Gráfica de la distribución total de personas reportadas \n por COVID-19 en Sur América")   # Establece nuevo título pero no muestra en gráfico


#ax.plot(time1, y1, 'go-', label='Mundo', color='red', marker='o')
#ax.plot(time2, y2, 'go-', label='China', color='black', marker='o')
#ax.plot(time3, y3, 'go-', label='Italia', color='blue', marker='o')
ax.plot(time, y4, 'go-', label='Colombia', color='red', marker='*')
ax.plot(time, y5, 'go-', label='Brasil', color='green', marker='.')
ax.plot(time, y6, 'go-', label='Ecuador', color='purple', marker='.')
ax.plot(time, y7, 'go-', label='Venezuela', color='brown', marker='.')
ax.plot(time, y8, 'go-', label='Peru', color='orange', marker='.')
ax.plot(time, y9, 'go-', label='Chile', color='gray', marker='.')

plt.legend(loc = "upper left") #Permite que las leyendas se muestren

#Rota las leyendas del eje x
ax.tick_params(axis='x', rotation=80)

#Imprime la tabla
fig = go.Figure(data=[go.Table(header=dict(values=['Fecha','COL','BRA','ECU','VEN','PER','CHI']),
                 cells=dict(values=[time, y4, y5, y6, y7, y8, y9]))
])

fig.show()
plt.grid(True)

plt.show()