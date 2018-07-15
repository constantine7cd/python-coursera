import os

class FileReader():

    def __init__(self, path):
        self.path = path

    def read(self):
        if os.path.isfile(self.path):
            with open(self.path, 'r') as f:
                try:
                    res = f.read()
                    return str(res)
                except IOError:
                    return ""
        else:
            return ""

def _main():
    reader = FileReader("in.txt")
    print(reader.read())

if __name__ == "__main__":
    _main()