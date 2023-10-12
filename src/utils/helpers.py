import json


def read_json(path_to_file: str):
    with open(path_to_file) as f:
        data = json.load(f)
    return data
