from twitter_followers import *
import json_utils


def run(screen_names, api):
    json_file_names = []

    for current_screen_name in screen_names:
        print(get_current_time_as_str()+" started processing "+current_screen_name)

        json_file = get_json_file_name(current_screen_name)

        graph = build_graph_of_followers(api, current_screen_name)
        print(get_current_time_as_str()+" "+current_screen_name+" followers added to graph")

        json_utils.write(json_file, graph)

        build_graph_of_followers_followers(api, graph[current_screen_name], json_file)
        print(get_current_time_as_str()+" "+current_screen_name+" followers followers added to graph")

        json_file_names.append(json_file)

        print(get_current_time_as_str()+" done processing "+current_screen_name+" resting for 5 sec\n")
        time.sleep(5)


def get_json_file_name(screen_name):
    return 'step2/step2-'+screen_name+'-graph.json'

