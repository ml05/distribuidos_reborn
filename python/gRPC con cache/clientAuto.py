import grpc
import swapi_pb2
import swapi_pb2_grpc
import csv
import time

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = swapi_pb2_grpc.SwapiServiceStub(channel)
        with open('dataset_ids.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                start_time = time.time()
                field = row['field']
                query = int(row['query'])
                if field == 'planets':
                    response = stub.GetPlanet(swapi_pb2.GetPlanetRequest(id=query))
                    print(response)
                    
                elif field == 'people':
                    response = stub.GetPerson(swapi_pb2.GetPersonRequest(id=query))
                    print(response)
                    
                elif field == 'species':
                    response = stub.GetSpecies(swapi_pb2.GetSpeciesRequest(id=query))
                    print(response)
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"tiempo: {elapsed_time:.4f} segundos")
                    

if __name__ == '__main__':
    run()
