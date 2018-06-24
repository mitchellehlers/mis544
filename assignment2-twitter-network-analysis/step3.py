from graphviz import *
import json_utils
import step2


def generate_graphvis_pdf(screen_name):
        file_to_process = step2.get_json_file_name(screen_name)
        graph = json_utils.read(file_to_process)

        dot = Digraph(comment='graph')

        for key in graph:
            next_screen_name = key
            followers = graph[key]
            dot.node(screen_name, next_screen_name)

            for follower in followers:
                dot.node(follower, follower)
                dot.edge(next_screen_name, follower)

        dot.render(get_graphvis_file_name(screen_name), view=True)


def get_graphvis_file_name(screen_name):
    return 'step3/step3-'+screen_name+'-graphvis.gv'