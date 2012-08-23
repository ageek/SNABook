import networkx.generators.small
import networkx as net
import matplotlib.pyplot as plot
from networkx.algorithms import traversal
from networkx import algorithms


g = networkx.generators.small.krackhardt_kite_graph()
g.number_of_edges()
g.number_of_nodes()
g.adjacency_list()
dict((x, g.neighbors(x)) for x in g.nodes())
# networkx.generators.small.krackhardt_kite_graph?
net.draw(g)
plot.show()

edges=traversal.dfs_edges(g,0)
list(edges)

edges = traversal.bfs_edges(g, 0)
bfs = list(edges)

net.draw(traversal.bfs_tree(g,0))
plot.show()

algorithms.shortest_path(g,0,7)
shorts = algorithms.all_pairs_shortest_path(g)
print "all shortest lengths", shorts
