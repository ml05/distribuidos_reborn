import redis
import requests
import json

# conexion con servidor local de redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)
CACHE_EXPIRATION_TIME = 300  # en segundos

def searchPerson(query):
    # busca si el resultado se encuentra almancenado en el cache
    cached_results = redis_client.get(query)
    # si se encuentra en el cache, lo retorna
    if cached_results:
        return json.loads(cached_results)

    # si no se encuentra en el cache, realiza la consulta a la API
    url = f'https://swapi.dev/api/people/?search={query}'
    response = requests.get(url)
    # si la consulta es exitosa, almacena el resultado en el cache
    if response.status_code == 200:
        results = response.json()
        redis_client.set(query, json.dumps(results))
        redis_client.expire(query, CACHE_EXPIRATION_TIME)
        return results
    else:
        return None

# este parametro se puede cambiar para probar el cache con otras consultas
query = 'luke'
results = searchPerson(query)
if results:
    for result in results['results']:
        print(result['name'])
        print(result['films'])
        print(result['url'])
else:
    print('No se encontraron resultados para su búsqueda.')
