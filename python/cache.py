import redis
import requests
import json
import time
import pandas as pd

# conexion con servidor local de redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# TTL del cache en segundos
# cache estatico (no se actualiza)
CACHE_EXPIRATION_TIME = 300  # en segundos

# cache dinamico 


# la funcion searchPerson realiza la consulta a la API y almacena el resultado en el cache
# ademas toma el tiempo de respuesta de la consulta
# para usar el mensaje usar searchPerson(query)[0]
# para usar el tiempo de respuesta usar searchPerson(query)[1]
def searchPerson(query):
    # se toma el tiempo apenas inicia la consulta
    start_time = time.time()
    # busca si el resultado se encuentra almancenado en el cache
    cached_results = redis_client.get(query)
    # si se encuentra en el cache, lo retorna
    if cached_results:
        end_time = time.time()
        response_time = end_time - start_time
        return json.loads(cached_results), response_time

    # si no se encuentra en el cache, realiza la consulta a la API
    url = f'https://swapi.dev/api/people/?search={query}'
    response = requests.get(url)
    # si la consulta es exitosa, almacena el resultado en el cache
    if response.status_code == 200:
        results = response.json()
        redis_client.set(query, json.dumps(results))
        redis_client.expire(query, CACHE_EXPIRATION_TIME)
        end_time = time.time()
        response_time = end_time - start_time
        return results, response_time
    else:
        end_time = time.time()
        response_time = end_time - start_time
        return None, response_time

# este parametro se puede cambiar para probar el cache con otras consultas
query = 'luke'
ans = searchPerson(query)
results = ans[0]
if results:
    for result in results['results']:
        print(result['name'])
        print(result['films'])
        print(result['url'])
else:
    print('No se encontraron resultados para su búsqueda.')

