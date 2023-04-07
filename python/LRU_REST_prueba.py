import redis
import requests
import json
from functools import lru_cache
from flask import Flask, request, jsonify

# esta es la conexión a REDIS de manera local
redis_client = redis.Redis(host='localhost', port=6379, db=0)
CACHE_EXPIRATION_TIME = 300  # en segundos

@lru_cache(maxsize=128)
def searchPerson(query):
    # pregunta a REDIS si hay resultados para la búsqueda
    cached_results = redis_client.get(query)
    # si existen los resultados, se retornan
    if cached_results:
        return json.loads(cached_results)
    # resultados obtenidos de la API
    url = f'https://swapi.dev/api/people/?search={query}'
    response = requests.get(url)
    # si la respuesta es exitosa, se almacenan en REDIS
    if response.status_code == 200:
        results = response.json()
        redis_client.set(query, json.dumps(results))
        redis_client.expire(query, CACHE_EXPIRATION_TIME)
        return results
    else:
        return None

app = Flask(__name__) # crea instancia FLASK

@app.route('/search', methods=['GET']) #Define la ruta para la API REST de busqueda
def search():
    query = request.args.get('query') # obtiene la query de la solicitud GET
    if not query:
        return jsonify({'error': 'Parametro de busqueda requerido'}), 400 # si no se especifica paramentro "error"
    results = searchPerson(query) #hace busqueda
    if results:
        return jsonify(results) # si se encuentra, retorna json
    else:
        return jsonify({'error': 'No se encontraron resultados para su búsqueda.'}), 404 #error si no se encuentra

if __name__ == '__main__': #ejecuta la aplicacion si se ejecuta el archivo
    app.run()
