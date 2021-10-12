from .json_serializer import json_serializer
from .pickle_serializer import pickle_serializer
from .toml_serializer import toml_serializer
from .yaml_serializer import yaml_serializer

def create_serializer(name):
    if name == 'json':
        return json_serializer()

    if name == 'pickle':
        return pickle_serializer()

    if name == 'toml':
        return toml_serializer()

    if name == 'yaml':
        return yaml_serializer()

    print("HZ Language")
    exit(1)

