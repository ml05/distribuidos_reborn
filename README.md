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
  2. Copiar la direccion URL generada (URL por defecto http://localhost:5000/ o http://127.0.0.1:5000/)
  3. Dentro de Postman hacer una peticion GET con la URL agregando search?field={field}&query={query} de la siguiente manera:
  ```
  http://localhost:5000/search?field=people&query=luke
  ```

- Para gRPC
correr server.py
correr client.py

para modificar inputs cambiar id en linea 8, Ejemplo
```
response = stub.GetPerson(swapi_pb2.GetPersonRequest(id=1))
response = stub.GetPerson(swapi_pb2.GetPersonRequest(id=2))
response = stub.GetPerson(swapi_pb2.GetPersonRequest(id=3))
```
