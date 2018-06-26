import snap
import json_utils

hash_to_screen_name_map = {}

def run(graph_file):
    merged_graph = json_utils.read(graph_file)

    snap_graph = snap.TNGraph.New()

    for key in merged_graph:
        screen_name = key
        followers = merged_graph[key]

        screen_name_hash = hash_screen_name(screen_name)

        if not snap_graph.IsNode(screen_name_hash):
            snap_graph.AddNode(screen_name_hash)

        for follower in followers:
            follower_hash = hash_screen_name(follower)

            if not snap_graph.IsNode(follower_hash):
                snap_graph.AddNode(follower_hash)

            snap_graph.AddEdge(screen_name_hash, follower_hash)

    nodes_count = snap_graph.GetNodes()
    edges_count = snap_graph.GetEdges()

    print("nodes count = "+str(nodes_count))
    print("edges count = "+str(edges_count))

    cluster_coeff = snap.GetClustCf(snap_graph, -1)
    print "Clustering coefficient: %f" % cluster_coeff

    return snap_graph


def get_screen_name_from_hash(hash_value):
    return hash_to_screen_name_map[hash_value]


def hash_screen_name(s):
    # creating a hash but limited to positive values only and limiting the length of the hash to 8 digits
    # used a a unique id for a screen_name
    hash_value = abs(hash(s)) % (10 ** 8)
    hash_to_screen_name_map[hash_value] = str(s)
    return hash_value



