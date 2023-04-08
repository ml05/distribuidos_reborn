# Sistemas Distribuidos

## Tarea 1

### Instalacion de componentes

- Se ocupa la ultima version alojada en Docker
  ```
  docker pull redis
  ```
- Se ejecuta un contenedor de Redis utilizando el comando:

  docker run --name redis -p 6379:6379 -d redis
- Se instalan las librerias: redis, json y requests
  ```
  pip install redis
  pip install simplejson
  python -m pip install requests
  ```


- Para utilizar REST con Postman
  ```
  pip install flask
  ```
  Luego seguir los siguientes pasos:
  1. Correr el codigo
  2. Copiar la direccion URL generada (URL por defecto http://localhost:5000/)
  3. Dentro de Postman hacer una peticion GET con la URL agregando search?query= {query} de la siguiente manera:
  ```
  http://localhost:5000/search?query=luke
  ```
