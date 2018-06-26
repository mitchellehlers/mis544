import snap
import json_utils


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


def hash_screen_name(s):
    return abs(hash(s)) % (10 ** 8)

