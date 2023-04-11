import grpc
import swapi_pb2
import swapi_pb2_grpc
import redis
import requests
from concurrent import futures

redis_host = 'localhost'
redis_port = 6379

class SwapiService(swapi_pb2_grpc.SwapiServiceServicer):
    def __init__(self):
        self.redis = redis.StrictRedis(host=redis_host, port=redis_port, db=0)

    def GetPerson(self, request, context):
        # Verificar si la información solicitada está en la caché de Redis
        person_key = f"person:{request.id}"
        person = self.redis.get(person_key)
        if person is not None:
            person = swapi_pb2.Person.FromString(person)
            return person

        # Si la información no está en la caché de Redis, hacer una solicitud HTTP a la API de Star Wars
        url = f"https://swapi.dev/api/people/{request.id}/"
        response = requests.get(url)

        # Verificar si la solicitud fue exitosa
        if response.status_code != 200:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Error al obtener información de la API de Star Wars: {response.status_code}")
            return None

        # Parsear la respuesta JSON y crear un objeto Person
        data = response.json()
        if 'results' in data:
            data = data['results'][0]
        person = swapi_pb2.Person(
            name=data['name'],
            birth_year=data['birth_year'],
            gender=data['gender'],
        )

        # Guardar la información en la caché de Redis
        self.redis.set(person_key, person.SerializeToString(), ex=300)

        return person

    def GetSpecies(self, request, context):
        # Verificar si la información solicitada está en la caché de Redis
        species_key = f"species:{request.id}"
        species = self.redis.get(species_key)
        if species is not None:
            species = swapi_pb2.Species.FromString(species)
            return species

        # Si la información no está en la caché de Redis, hacer una solicitud HTTP a la API de Star Wars
        url = f"https://swapi.dev/api/species/{request.id}/"
        response = requests.get(url)

        # Verificar si la solicitud fue exitosa
        if response.status_code != 200:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Error al obtener información de la API de Star Wars: {response.status_code}")
            return None

        # Parsear la respuesta JSON y crear un objeto Species
        data = response.json()
        if 'results' in data:
            data = data['results'][0]
        species = swapi_pb2.Species(
            name=data['name'],
            classification=data['classification'],
            average_lifespan=data['average_lifespan'],
            language=data['language'],
            
        )

        # Guardar la información en la caché de Redis
        self.redis.set(species_key, species.SerializeToString(), ex=300)

        return species

    def GetPlanet(self, request, context):
        # Verificar si la información solicitada está en la caché de Redis
        planet_key = f"planet:{request.id}"
        planet = self.redis.get(planet_key)
        if planet is not None:
            planet = swapi_pb2.Planet.FromString(planet)
            return planet

        # Si la información no está en la caché de Redis, hacer una solicitud HTTP a la API de Star Wars
        url = f"https://swapi.dev/api/planets/{request.id}/"
        response = requests.get(url)

        # Verificar si la solicitud fue exitosa
        if response.status_code != 200:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Error al obtener información de la API de Star Wars: {response.status_code}")
            return None

        # Parsear la respuesta JSON y crear un objeto Planet
        data = response.json()
        planet = swapi_pb2.Planet(
            name=data['name'],
            diameter=data['diameter'],
            climate=data['climate']
        )

        # Guardar la información en la caché de Redis
        self.redis.set(planet_key, planet.SerializeToString(), ex=300)

        return planet



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    swapi_pb2_grpc.add_SwapiServiceServicer_to_server(SwapiService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC en ejecución...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()