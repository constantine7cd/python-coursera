import asyncio
import time

class Client:

    message_amount = 3

    def __init__(self, host, port, timeout=None):
        self.__host = host
        self.__port = int(port)
        #timeout

        '''It is necessary to resolve problem with:      
        -timeout
        '''
    def __run_read(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.read_coro(loop))
        loop.close()

    def __run_write(self, message):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.write_coro(message, loop))
        loop.close()

    async def write_coro(self, message, loop):
        _, writer = await asyncio.open_connection(self.__host, self.__port, loop=loop)
        writer.write(message.encode())
        writer.close()

    async def read_coro(self, loop):
        reader, _ = await asyncio.open_connection(self.__host, self.__port, loop=loop)
        data = await reader.read(1024)
        self.message = data.decode()

    def put(self, name, value, timestamp=None):

        self.timestamp = timestamp or str(int(time.time()))
        self.name = name
        self.value = float(value)

        #try:
        self.__run_write('put {} {} {}\n'.format(name, value, timestamp))
        #except:
            #raise ClientError()

    def get(self, key):
        #try:
        self.__run_read()
        #except:
            #raise ClientError()
        metrics_str = self.message.split('\n')
        data = {}

        for i in metrics_str:
            elem = i.split(" ")
            if len(elem) is self.message_amount:
                if elem[0] not in data:
                    data[elem[0]] = [(float(elem[1]), int(elem[2]))]
                else:
                    data[elem[0]].append((float(elem[1]), int(elem[2])))

        if key is "*":
            return data
        elif key in data:
            return { key : data[key]}
        else:
            return {}

class ClientError:
    """ Errors with Client work. """
    def __init__(self, *args, **kwargs):  # real signature unknown
        pass

    @staticmethod  # known case of __new__
    def __new__(*args, **kwargs):  # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

'''timeout and ClientError and that is all'''

