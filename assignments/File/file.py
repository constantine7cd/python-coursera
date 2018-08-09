import os
import tempfile

class File:

    def __init__(self, path):
        self.path = path

        if not os.path.isfile(path):
            with open(path, "w") as f:
                pass

    def __add__(self, other):
        new_path = os.path.join(tempfile.gettempdir(), 'sum.txt')
        new = File(new_path)

        with open(self.path, "r") as f:
            self_info = f.read()

        with open(other.path, "r") as g:
            other_info = g.read()

        with open(new.path, "r+") as n:
            n.write(self_info)
            n.write(other_info)

        return new


    def __str__(self):
        return self.path

    def __iter__(self):
        with open(self.path, "r") as f:
            data = f.readlines()

        self.data = iter(data)

        return self.data



    def __next__(self):
        next(self.data)


    def write(self, str):
        with open(self.path, "a") as f:
            f.write(str)



'''a = File('a.txt')
b = File('b.txt')

a.write('oh my cash\n')
a.write('some thoughts about this\n')
a.write('Woow\n')
a.write('yeeep\n')
b.write('summer time\n')

#c = a + b
#print(c)


for line in a:
    print(line)'''


