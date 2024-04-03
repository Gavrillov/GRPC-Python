import grpc
import protocol.gripd_pb2 as pb2
import protocol.gripd_pb2_grpc as pb2_grpc
from flask import Flask, render_template, request
import uuid

app = Flask(__name__)


try:
    channel = grpc.insecure_channel('localhost:50051')
    stub = pb2_grpc.MyServiceStub(channel)
except grpc.RpcError as e:
    print(f"Ошибка при подключении к серверу gRPC: {e}")

@app.route('/', methods=['GET', 'POST'])
def log_data():
    UUID = str(uuid.uuid1())
    try:
        if request.method == 'POST':
            Level = request.form.get('Level')
            discriptionlevel = request.form.get('discriptionlevel')
            returned = request.form.get('message')
            reques = pb2.HelloRequest(uuid = UUID, Level = Level, discriptionlevel = discriptionlevel, returned = returned)
            response = stub.SayHello(reques)
            try:
                with open('Files/Requests.txt', 'a') as file:
                    file.write(response.message)
            except IOError:
                print('ОШИБКА')


        elif request.method == 'GET':
            with open('Files/Requests.txt', 'r') as f:
                lines = f.readlines()
                last_three_lines = lines[-3:]
                for line in last_three_lines:
                    print(line, end='')



    except Exception as e:
        print(f"Ошибка при обработке запроса на сервере Flask: {e}")

    return render_template('index.html')

try:
    if __name__ == '__main__':
        app.run(host='0.0.0.0')
except Exception as e:
    print(f"Ошибка при запуске Flask-приложения: {e}")




