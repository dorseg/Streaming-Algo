import networkx as nx
import numpy as np
from random import randrange
from components.Label import Label
from construct import construct
from math import log


def make_spanner(G, t=None):
    """
    The algorithm specified in the article.
    :param G: Graph
    :param t: an integer positive parameter t
    :return: Gs: (2t-1) spanner of G
    """
    spanner = []
    # TODO remove?
    if t is None:
        t = randrange(1, 10)  # pick randomly stretch factor
    init(G, t)  # preprocess
    for e in G.edges():  # process
        read_edge(e)
    for v in G.nodes():  # End
        spanner.extend(v.get_sp())

    #  build the 2t-1 spanner graph Gs
    Gs = nx.Graph()
    Gs.add_nodes_from(G.nodes())
    Gs.add_edges_from(spanner)
    return Gs


def read_edge(e):
    """
    The streaming model algorithm of constructing a sparse (2t-1) spanner
    :param e: Edge to process
    :return: void
    """
    u, v = max(e[0], e[1]), min(e[0], e[1])  # let u be the bigger vertex
    P_u = u.get_label()
    M_v = v.get_table()
    B_Pu = P_u.get_base_val()
    Sp_v = v.get_sp()
    if P_u.is_selected():
        v.update_label(P_u)
        Sp_v.append(e)
    elif B_Pu not in M_v:
        M_v.add(B_Pu)
        Sp_v.append(e)


def init(G, t):
    """
     Initialized graph as described below:
         each vertex v in V is assigned by:
            1. unique identifers from the set {1,2,...,n} for I(v).
            2. non-negative integer radius r(v).
            3. let the label of v be I(v)
    :param G: input Graph
    :param t: integer positive number, represent the stretch
    :return void
    """
    N = G.number_of_nodes()
    i = 1
    for v in G.nodes():
        v.set_index(i)
        v.set_label(Label(0, i, v, N))
        i += 1
        v.set_radius(choose_radius(N, t))


def choose_radius(N, t):
    """
    :param N: number of nodes
    :param t: stretch factor
    :return: non-negative integer radius picked from the truncated geometric probability distribution
    """
    p = pow(log(N,2)/N, 1.0/t)
    r = np.random.geometric(p)
    if r >= t:
        r = t-1
    return r











