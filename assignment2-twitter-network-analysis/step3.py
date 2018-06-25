from graphviz import *
import json_utils
import step2


def run(screen_name, step='step3'):
        file_to_process = step2.get_json_file_name(screen_name)
        graph = json_utils.read(file_to_process)
        generate_graphvis_pdf(graph, screen_name, step)


def generate_graphvis_pdf(graph, graphvis_name, step='step3'):
    dot = Digraph(comment='graph')

    for key in graph:
        next_screen_name = key
        followers = graph[key]
        dot.node(next_screen_name, next_screen_name)

        for follower in followers:
            dot.node(follower, follower)
            dot.edge(next_screen_name, follower)

    dot.render(get_graphvis_file_name(graphvis_name, step), view=True)


def get_graphvis_file_name(screen_name, step):
    return step+'/'+step+'-'+screen_name+'-graphvis.gv'

