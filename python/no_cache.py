import requests
import json
import time
from flask import Flask, request, jsonify

def searchPerson(field, query):
    # realiza la consulta a la API
    url = f'https://swapi.dev/api/{field}/?search={query}'
    response = requests.get(url)
    # si la consulta es exitosa la retorna
    if response.status_code == 200:
        results = response.json()
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

