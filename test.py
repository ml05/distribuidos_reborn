# programa para calcular la frecuencia de cada personaje
import pandas as pd

# Lee el archivo CSV en un DataFrame de pandas
df = pd.read_csv('/Users/matiasaguileralienlaff/Documents/distribuidos/distribuidos_reborn/dataset.csv')

# Obtiene la frecuencia de cada valor en una columna específica del DataFrame
frequencies = df['character'].value_counts()

# Crea un archivo de texto y escribe las frecuencias de los valores en él
with open('frecuencias.txt', 'w') as f:
    for index, value in frequencies.items():
        f.write(f"{index}: {value}\n")
