import grpc
import swapi_pb2
import swapi_pb2_grpc
import redis
import requests

redis_host = 'localhost'
redis_port = 6379

class SwapiService(swapi_pb2_grpc.SwapiServiceServicer):
    def __init__(self):
        self.redis = redis.StrictRedis(host=redis_host, port=redis_port, db=0)

    def get_person(self, request, context):
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
        person = swapi_pb2.Person(
            id=data['id'],
            name=data['name'],
            birth_year=data['birth_year'],
            gender=data['gender'],
            films=data['films'],
        )

        # Guardar la información en la caché de Redis
        self.redis.set(person_key, person.SerializeToString())

        return person

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    swapi_pb2_grpc.add_SwapiServiceServicer_to_server(SwapiService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC en ejecución...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
