import json
from os import path

def exists_at(fp):
    return path.exists(fp)

def read_from_file(fp):
    with open(fp) as f:
        return json.loads(f.read())

def persist_to_file(config, fp):
    with open(fp, "w") as f:
        f.write(json.dumps(config))

def read_from_user():
    cfg = {}
    print("--- Configuration ---")
    cfg["host"] = input("Database host: ")
    cfg["user"] = input("Database user: ")
    cfg["passwd"] = input("Database password: ")
    return cfg
