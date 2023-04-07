# archivo para generar dataset a partir de los personajes de Star Wars
# con el archivo generado, se espera tener una muestra de posibles busquedas

import pandas as pd
import random

# Cargar el dataset original desde el archivo CSV
dataset = pd.read_csv('dataset_original.csv')

# Tomar una muestra aleatoria de 1000 filas
muestra_aleatoria = dataset.sample(n=1000, random_state=random.seed())

# Crear un nuevo archivo CSV y escribir la muestra aleatoria en el archivo
muestra_aleatoria.to_csv('test.csv', index=False)