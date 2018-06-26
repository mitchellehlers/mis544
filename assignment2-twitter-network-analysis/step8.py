import step7
import snap
import heapq


def run(snap_graph):
    page_rank = snap.TIntFltH()
    snap.GetPageRank(snap_graph, page_rank)

    node_page_ranks = []
    node_page_rank_name_map = {}
    for node in page_rank:
        value = page_rank[node]
        if value not in node_page_ranks:
            node_page_ranks.append(value)
        node_page_rank_name_map[value] = step7.get_screen_name_from_hash(node)

    top_ten_page_ranks = heapq.nlargest(10, node_page_ranks)

    print "\nTop 10 page ranks from the merged graph =>"
    for top_node in top_ten_page_ranks:
        print node_page_rank_name_map[top_node], top_node