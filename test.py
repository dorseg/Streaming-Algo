import networkx as nx


def test_spanner(G, Gs, t):
    """
    :param G: Graph
    :param Gs: spanner of G
    :param t: stretch factor
    :return: True if Gs is (2t-1)-spanner of G, False otherwise.
    """
    if not nx.is_connected(Gs):
        ans = False
    else:
        lengths_G = nx.all_pairs_shortest_path_length(G)
        lengths_Gs = nx.all_pairs_shortest_path_length(Gs)
        stretch = 2*t-1
        ans = True
        for u in lengths_Gs:
            if not ans:
                break
            for v in lengths_Gs[u]:
                if lengths_Gs[u][v] > stretch * lengths_G[u][v]:
                    ans = False
                    break

    if ans:
        print "Test result: Success!" + u"\u263A"
    else:
        print "Test result: Fail" + u"\u2639"


