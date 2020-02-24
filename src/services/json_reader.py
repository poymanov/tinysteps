import json


def read_json(file_path):
    with open(file_path) as file:
        return file.read()


def load_json(json_data):
    return json.loads(json_data)
