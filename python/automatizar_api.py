import requests
import time

# Definir la URL de la API
url = 'https://swapi.dev/api/people/'

# Definir la cantidad de solicitudes a realizar
n = 10

# Definir el tiempo entre cada solicitud
time_between_requests = 5 # segundos

# Hacer n solicitudes GET a la API con pausas entre cada solicitud
for i in range(n):
    response = requests.get(url)
    if response.status_code == 200:
        print("Solicitud exitosa.")
    else:
        print("Error en la solicitud.")
    
    # Esperar un tiempo antes de hacer la siguiente solicitud
    time.sleep(time_between_requests)
