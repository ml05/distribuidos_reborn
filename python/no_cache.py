import requests
import json
import time

def searchPerson(query):
    start_time = time.time()
    # realiza la consulta a la API
    url = f'https://swapi.dev/api/people/?search={query}'
    response = requests.get(url)
    # si la consulta es exitosa la retorna
    if response.status_code == 200:
        results = response.json()
        end_time = time.time()
        response_time = end_time - start_time
        return results, response_time
    else:
        end_time = time.time()
        response_time = end_time - start_time
        return None, response_time

# este parametro se puede cambiar para probar el cache con otras consultas
query = 'luke'
results = searchPerson(query)[0]
# if results:
#     for result in results['results']:
#         print(result['name'])
#         print(result['films'])
#         print(result['url'])
# else:
#     print('No se encontraron resultados para su búsqueda.')

# toma de tiempo en ejecucion de una consulta
response_time = searchPerson(query)[1]

print(f'Tiempo de respuesta: {response_time:.2f} segundos')
if response_time > 0.05:
    # Si el tiempo de respuesta es mayor a 5 segundos, registra este tiempo en un archivo de log o en una base de datos
    print('El tiempo de respuesta es mayor a 5 segundos. Se debe investigar.')