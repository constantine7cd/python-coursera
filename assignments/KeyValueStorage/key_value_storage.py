import argparse
import os
import tempfile
import json

def is_file_exists(fname):
    return os.path.isfile(fname)

def is_file_empty(fname):
    return os.path.getsize(fname) == 0

def create_file(fname):
    with open(fname, 'w') as f:
        pass

def write_to_storage(storage_path, key, value):
    d = dict()

    if not is_file_empty(storage_path):
        with open(storage_path, 'r') as f:
            d = json.load(f)

    if key not in d:
        d[key] = [value]
    elif value not in d[key]:
        d[key].append(value)

    with open(storage_path, 'w') as f:
        json.dump(d, f)

def read_from_storage(storage_path, key):

    if not is_file_empty(storage_path):

        with open(storage_path, 'r') as f:
            d = json.load(f)

        if key in d:
            keyword_list = d[key]

            print(*keyword_list, sep=', ')

def key_value():
    parser = argparse.ArgumentParser(description="key value storage")

    parser.add_argument("-k", "--key", type = str, action="store")
    parser.add_argument("-v", "--value", type = str, action="store")

    args = parser.parse_args()


    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

    if not is_file_exists(storage_path):
        create_file(storage_path)

    if args.key and args.value:
        write_to_storage(storage_path, args.key, args.value)
    elif args.key:
        read_from_storage(storage_path, args.key)

if __name__ == "__main__":
    key_value()



  