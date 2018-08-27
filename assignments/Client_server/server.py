import asyncio


class ClientServerProtocol(asyncio.Protocol):

    put_amount = 4
    get_amount = 2
    server_data = {}

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())

    def process_data(self, data):
        split_data = data.split()
        error = 'error\nwrong command\n\n'
        ok = 'ok\n\n'

        if split_data[0] == 'put' and len(split_data) == self.put_amount:
            '''put case'''
            try:
                key = split_data[1]
                value = float(split_data[2])
                timestamp = int(split_data[3])

                data = (timestamp, value)

                if key not in self.server_data:
                    self.server_data[key] = [data]
                elif data not in self.server_data[key]:
                    self.server_data[key].append(data)

            except ValueError:
                return error

            return ok
        elif split_data[0] == 'get' and len(split_data) == self.get_amount:
            '''get case'''
            key = split_data[1]
            res = 'ok\n'
            if key == '*':
                '''full list of data'''
                for k in self.server_data:
                    for i in self.server_data[k]:
                        res += '{} {} {}\n'.format(k, i[1], i[0])

            elif key in self.server_data:
                for i in self.server_data[key]:
                    res += '{} {} {}\n'.format(key, i[1], i[0])

            res += '\n'

            return res

        else:
            return error



def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


