import grpc
import swapi_pb2
import swapi_pb2_grpc
import csv

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = swapi_pb2_grpc.SwapiServiceStub(channel)
        with open('dataset_id.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            contador = 2
            for row in reader:
                
                field = row['field']
                query = int(row['query'])
                if field == 'planets':
                    response = stub.GetPlanet(swapi_pb2.GetPlanetRequest(id=query))
                    print(response)
                    contador=contador+1
                    print (contador)
                elif field == 'people':
                    response = stub.GetPerson(swapi_pb2.GetPersonRequest(id=query))
                    print(response)
                    contador=contador+1
                    print (contador)
                elif field == 'species':
                    response = stub.GetSpecies(swapi_pb2.GetSpeciesRequest(id=query))
                    print(response)
                    contador=contador+1
                    print (contador)

if __name__ == '__main__':
    run()
