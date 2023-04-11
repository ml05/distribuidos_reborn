# archivo para generar dataset a partir de los personajes de Star Wars
# con el archivo generado, se espera tener una muestra de posibles busquedas

import pandas as pd
import random

# Cargar el archivo CSV
datos = pd.read_csv('/Users/matiasaguileralienlaff/Documents/distribuidos/distribuidos_reborn/dataset/sw_ids.csv')

# Generar una lista de 1000 números aleatorios enteros entre 0 y 51
indices = [random.randint(0, 146) for i in range(3000)]

# Crear una nueva lista vacía para la muestra
muestra = []

# Iterar a través de los números aleatorios y agregar el valor de la fila correspondiente a la lista de muestra
for i in indices:
    muestra.append(datos.iloc[i])

# Escribir la lista de muestra en un nuevo archivo CSV
pd.DataFrame(muestra).to_csv('test.csv', index=False)

# CALCULAR LA FRECUENCIA DE CADA PERSONAJE EN EL DATASET
# Lee el archivo CSV en un DataFrame de pandas
df = pd.read_csv('/Users/matiasaguileralienlaff/Documents/distribuidos/distribuidos_reborn/dataset.csv')

# # Obtiene la frecuencia de cada valor en una columna específica del DataFrame
# frequencies = df['field'].value_counts()

# # Crea un archivo de texto y escribe las frecuencias de los valores en él
# with open('frecuencias.txt', 'w') as f:
#     for index, value in frequencies.items():
#         f.write(f"{index}: {value}\n")