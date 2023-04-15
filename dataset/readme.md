# Sobre los archivos de la carpeta Dataset

Los arhivos almacenados en esta carpeta tienen las siguientes funcionalidades:

- dataset_ids.csv: contiene el dataset de 3000 consultas, utilizando un ID. El uso esta limitado a gRPC.

- dataset.csv: contiene las 3000 consutlas, pero del estilo {field,query}, para ser utilizado con REST.

- starwars.csv: archivo principal con consultas unicas y posibles. Al utilizarlas entregan un codigo 200.

- sw_ids.csv: al igual que la anterior, pero esta vez con ID asociado.

- generarDataset.py: programa para generar los dataset de 3000 consultas basados en los archivos starwars.csv o sw_ids.csv, los cuales son repetidos de manera aleatoria.