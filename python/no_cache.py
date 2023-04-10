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

# REST API
app = Flask(__name__) # crea instancia FLASK

@app.route('/search', methods=['GET']) #Define la ruta para la API REST de busqueda
def search():
    field = request.args.get('field') # obtiene el campo de la solicitud GET
    query = request.args.get('query') # obtiene la query de la solicitud GET
    if not query:
        return jsonify({'error': 'Parametro de busqueda requerido'}), 400 # si no se especifica paramentro "error"
    results = searchPerson(field, query) #hace busqueda
    if results:
        return jsonify(results) # si se encuentra, retorna json
    else:
        return jsonify({'error': 'No se encontraron resultados para su búsqueda.'}), 404 #error si no se encuentra

if __name__ == '__main__': #ejecuta la aplicacion si se ejecuta el archivo
    app.run()
