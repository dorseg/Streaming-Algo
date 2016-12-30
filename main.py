import streaming as st
import matplotlib.pyplot as plt
from test import test_spanner

# TODO 1. use argparse for Elkin
# TODO 2. loop that picks Graph and run the algorithm
# TODO 3. what information should be printed

N = 200
t = 3
G = st.construct(N)
Gs = st.make_spanner(G, t)

print "Number of nodes: {}\nParameter t: {}".format(N, t)
print "Number of edges in G: {}\nNumber of edges in Gs: {}".format(G.number_of_edges(), Gs.number_of_edges())
ans = test_spanner(G, Gs, t)

st.nx.draw(G)
plt.show()

st.nx.draw(Gs)
plt.show()




