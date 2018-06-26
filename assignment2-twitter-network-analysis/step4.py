import json_utils
import twitter_followers
import step2
import step3


def run(graph_name, screen_names, step='step4'):
    merged_graph = {}
    for screen_name in screen_names:
        file_name = step2.get_json_file_name(screen_name)
        graph = json_utils.read(file_name)
        merged_graph = twitter_followers.merge_two_graphs(graph, merged_graph)

    json_utils.write(step+"/"+graph_name+".json", merged_graph)
    step3.generate_graphvis_pdf(merged_graph, graph_name, step)


