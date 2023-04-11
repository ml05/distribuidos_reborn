import grpc
import swapi_pb2
import swapi_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = swapi_pb2_grpc.SwapiServiceStub(channel)
        response = stub.GetSpecies(swapi_pb2.GetSpeciesRequest(id=3))
    print(response)

if __name__ == '__main__':
    run()
