import json
import yaml


def dump_data(data: str, file_path: str):
    with open(file_path, "w") as f:
        f.write(data)


def load_json(file_path: str) -> dict:
    with open(file_path, "r") as f:
        data = json.loads(f.read())
    return data


def load_yaml(file_path: str) -> dict:
    with open(file_path, "r") as stream:
        return yaml.safe_load(stream)
