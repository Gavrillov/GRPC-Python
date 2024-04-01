from datetime import datetime
import socket
import grpc
from concurrent import futures
import protocol.greet_pb2 as pb2
import uuid
import protocol.greet_pb2_grpc as pb2_grpc
import os


class MyService(pb2_grpc.MyServiceServicer):
    def SayHello(self, reques, context):
        try:
            UUID = uuid.uuid1()
            Level = reques.Level
            discriptionlevel = reques.discriptionlevel
            returned = reques.returned
            status = reques.status
            message = (f'Запрос обработан \n'
                       f'id Запроса - {UUID}\n'
                       f'Статус записи в файл - {status}\n'
                       f'                                      \n')
            input_file(reques, UUID)
            return pb2.HelloResponse(message=message)
        except Exception as e:
            print(f"Ошибка при обработке запроса: {e}")
            return pb2.HelloResponse(message="Ошибка при обработке запроса")


def input_file(request, UUID):
    try:
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')
        project_name = os.getenv('PROJECT_NAME')
        contaner_name = socket.gethostname()
        hostname = socket.gethostname()
        contaner_ip = socket.gethostbyname(hostname)

        with open('Files/Requests.log', 'a') as file:
            file.write(f'UUID = "{UUID}"\n,'
                       f'serverEventDatetime="{current_date}", project="{project_name}",'
                       f' podName="{contaner_name}", ip="{contaner_ip}", logLevel="{request.Level}", '
                       f'levelStr="{request.discriptionlevel}", returned= "{request.returned}"' + "\n")
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")



# Создаём сервер gRPC
try:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_MyServiceServicer_to_server(MyService(), server)

    # Задаём адрес и порт на котором будем слушать сервер
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Сервер запущен на порту 50051")
    server.wait_for_termination()




except Exception as e:
    print(f"Ошибка при запуске сервера: {e}")