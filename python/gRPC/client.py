import grpc
import swapi_pb2
import swapi_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = swapi_pb2_grpc.SwapiServiceStub(channel)
    person = stub.GetPerson(swapi_pb2.GetPersonRequest(id=1))
    print(f"ID: {person.id}")
    print(f"Nombre: {person.name}")
    print(f"Año de nacimiento: {person.birth_year}")
    print(f"Género: {person.gender}")
    print("Películas:")
    for film in person.films:
        print(film)

if __name__ == '__main__':
    run()
