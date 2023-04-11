# Sistemas Distribuidos

## Tarea 1
Limites de la API Star Wars:
- 60 Planetas
- 83 Personas (id 17 vacio)
- 37 Especies

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

- Para gRPC (solo puede haber 1 server corriendo a la vez)

1.correr server.py
```
python server.py
```
2. correr clientAuto para recorrer el dataset o clientIndividual para correr querys especificas (se pueden correr multiples clientes a la vez)
```
python clientAuto
python clientIndividual
```

para modificar inputs en clientIndividual cambiar id en linea 8, Ejemplo
```
response = stub.GetPerson(swapi_pb2.GetPersonRequest(id=1))
response = stub.GetPerson(swapi_pb2.GetPersonRequest(id=2))
response = stub.GetPerson(swapi_pb2.GetPersonRequest(id=3))
```
para modificar inputs en clientAuto modificar dataset_id.csv
