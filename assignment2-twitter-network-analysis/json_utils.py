import json


def write(filename, data):
    with open(filename, 'w') as fp:
        json.dump(data, fp)


def append(filename, data):
    with open(filename) as f:
        graph = json.load(f)

    graph.update(data)

    with open(filename, 'w') as fp:
        json.dump(graph, fp)


