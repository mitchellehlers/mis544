import json


def write(filename, data):
    with open(filename, 'w') as fp:
        json.dump(data, fp)


def append(filename, data):
    with open(filename) as f:
        json_data = json.load(f)

    json_data.update(data)

    with open(filename, 'w') as fp:
        json.dump(json_data, fp)


def read(filename):
    with open(filename) as f:
        json_data = json.load(f)

    return json_data


