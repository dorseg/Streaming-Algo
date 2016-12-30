from components.Vertex import Vertex
from streaming import nx

def construct(nodes_num):
    """
    :param: nodes_num: the number of nodes in the constructed graph.
    :return: random graph G = (V,E) according to Erdos-Renyi model.
    """
    #  TODO construct
    G = nx.fast_gnp_random_graph(nodes_num, 0.5)
    nx.relabel_nodes(G, mapping=Vertex, copy=False)
    return G

