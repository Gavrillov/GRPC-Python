import json
import socket
import grpc
import protocol.gripd_pb2 as pb2
import protocol.gripd_pb2_grpc as pb2_grpc
from flask import Flask, render_template, request, jsonify, redirect
import uuid


app = Flask(__name__)

with open('Files/config.json', 'r') as server_config_file:
    server_conf = json.load(server_config_file)

try:
    channel = grpc.insecure_channel(f'{server_conf["gRPC_HOST"]}: {server_conf["Grpc_port"]}')
    stub = pb2_grpc.MyServiceStub(channel)
except grpc.RpcError as e:
    print(f"Ошибка при подключении к серверу gRPC: {e}")

@app.route('/', methods=['GET', 'POST'])
def log_data():
    UUID = str(uuid.uuid1())
    contaner = socket.gethostname()
    hostname = socket.gethostname()
    contanerip = socket.gethostbyname(hostname)

    try:
        if request.method == 'POST':
            Level = request.form.get('Level')
            discriptionlevel = request.form.get('discriptionlevel')
            returned = request.form.get('message')
            reques = pb2.HelloRequest(uuid = UUID, Level = Level, discriptionlevel = discriptionlevel,
                                      returned = returned, contaner = contaner, contanerip = contanerip)
            response = stub.SayHello(reques)
            new_data = {"uuid": response.uuid, "Level": response.LogStatus}
            try:
                with open('Files/data.json', 'r', encoding='utf8') as file:
                    data = json.load(file)
                    data['logs'].append(new_data)
            except (FileNotFoundError, json.JSONDecodeError):
                data = {"logs": [new_data]}

            try:
                with open('Files/data.json', 'w', encoding='utf8') as out_file:
                    json.dump(data, out_file, ensure_ascii=False, indent=2)
            except IOError:
                print('Ошибка при записи в файл')

            return redirect('/data')
    except Exception as e:
        print(f"Ошибка при обработке запроса на сервере Flask: {e}")

    return render_template('index.html')

@app.route('/data', methods=['GET'])
def get_data():
    if request.method == 'GET':
        with open('Files/data.json') as file:
           data = json.load(file)
        return jsonify(data)


try:
    if __name__ == '__main__':
        app.run(host='0.0.0.0')
except Exception as e:
    print(f"Ошибка при запуске Flask-приложения: {e}")




