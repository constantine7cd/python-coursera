import time
import socket

class Client:

    message_amount = 3

    def __init__(self, host, port, timeout=None):
        self.__host = host
        self.__port = int(port)

        self.__timeout  = timeout


    def __read_write(self, message):
        with socket.create_connection((self.__host, self.__port), self.__timeout) as sock:
            try:
                sock.sendall(message.encode())
                self.response = sock.recv(1024).decode()

                if self.response == 'error\nwrong command\n\n':
                    raise ClientError()
            except socket.timeout:
                raise ClientError()
            except socket.error:
                raise ClientError()


    def put(self, name, value, timestamp=None):

        self.timestamp = timestamp or str(int(time.time()))
        self.name = name
        self.value = float(value)
        self.__read_write('put {} {} {}\n'.format(name, value, timestamp))


    def get(self, key):
        self.__read_write('get {}\n'.format(key))
        metrics_str = self.response.split('\n')
        data = {}

        for i in metrics_str:
            elem = i.split(" ")
            if len(elem) is self.message_amount:
                if elem[0] not in data:
                    data[elem[0]] = [(int(elem[2]), float(elem[1]))]
                else:
                    data[elem[0]].append((int(elem[2]), float(elem[1])))

        if key is "*":
            return data
        elif key in data:
            return { key : data[key]}
        else:
            return {}

class ClientError(Exception):
    pass
