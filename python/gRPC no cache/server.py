import grpc
import swapi_pb2
import swapi_pb2_grpc
import redis
import requests
from concurrent import futures

class SwapiService(swapi_pb2_grpc.SwapiServiceServicer):

    def GetPerson(self, request, context):

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

        return person

    def GetSpecies(self, request, context):

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

        return species

    def GetPlanet(self, request, context):

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