# Sistemas Distribuidos

## Tarea 1

### Instalacion de componentes

- Se ocupa la ultima version alojada en Docker

  docker pull redis
- Se ejecuta un contenedor de Redis utilizando el comando:

  docker run --name redis -p 6379:6379 -d redis
- Se instalan las librerias: redis, json y requests

  pip install redis
  pip install simplejson
  python -m pip install requests
