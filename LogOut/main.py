import json
from datetime import datetime
import grpc
from concurrent import futures
import protocol.greet_pb2 as pb2
import protocol.greet_pb2_grpc as pb2_grpc

with open('config.json', 'r') as server_config_file:
    server_conf = json.load(server_config_file)


class MyService(pb2_grpc.MyServiceServicer):
    def SayHello(self, request, context):
        UUID = request.uuid
        status = input_file(request)
        return pb2.HelloResponse(uuid=UUID, LogStatus=status)


def input_file(request):
    try:
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
        project_name = f'{server_conf["Project_name"]}'

        with open('Files/Requests.log', 'a') as file:
            file.write(f'serverEventDatetime="{current_date}", project="{project_name}",'
                       f' podName="{request.container}", ip="{request.containerip}", logLevel="{request.Level}", '
                       f'levelStr="{request.discriptionlevel}", returned="{request.returned}"' + "\n")
        status = 201
    except Exception as e:
        status = 501
        print(f"Ошибка при записи в файл: {e}")

    return status


# Создаём сервер gRPC
try:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_MyServiceServicer_to_server(MyService(), server)

    # Задаём адрес и порт на котором будем слушать сервер
    server.add_insecure_port(f'{server_conf["gRPC_HOST"]}:{server_conf["Grpc_port"]}')
    server.start()
    print("Сервер запущен")
    server.wait_for_termination()

except Exception as e:
    print(f"Ошибка при запуске сервера: {e}")
