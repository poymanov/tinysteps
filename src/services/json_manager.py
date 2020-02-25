import json
import os


def read_json(file_path):
    create_file(file_path)

    with open(file_path) as file:
        return file.read()


def save_json(file_path, data):
    create_file(file_path)

    with open(file_path, 'w') as file:
        return file.write(data)


def load_json(json_data):
    return json.loads(json_data)


def dump_json(data):
    return json.dumps(data)


def create_file(file_path):
    if not os.path.exists(os.path.dirname(file_path)) or not os.path.exists(file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as f:
            f.write(dump_json([]))
