import networkx as net
import matplotlib.pyplot as plot
g=net.read_pajek('russians.net')
len(g)

deg=net.degree(g)
print  deg['valerois']
print  min(deg.values())
print  max(deg.values())

### This function returns a sorted degree list -- useful for celebrity-spotting
def sorted_map(map):
	ms = sorted(map.iteritems(), key=lambda (k,v): (-v,k))
	return ms

ds=sorted_map(deg)
### Top 10 people in the list
print ds[0:9]

h=plot.hist(deg.values(),100)        ## display a histogram of node degrees 
plot.loglog(h[1][1:],h[0])           ## plot the same histogram in Log-Log space
plot.show()

def trim_degrees(g, degree=1):
	g2=g.copy()
	d=net.degree(g2)
	for n in g2.nodes():
		if d[n]<=degree: g2.remove_node(n)
	return g2


#1. First plot the trimmed down network

#core=trim_degrees(g)
#print len(core)

#core2=trim_degrees(g,degree=2)
#print len(core2)

#core3=trim_degrees(g,degree=3)
#print len(core3)

core10=trim_degrees(g,degree=10)
len(core10)


net.draw(core10)
plot.show()

#2. Closeness (gossiper)

c=net.closeness_centrality(core10)
#sort the results using a function from previous section
cs=sorted_map(c)
#top-10 gossipers
cs[:10]

all_values = [row[1] for row in cs]
plot.hist(all_values,100)
plot.show()


#3. Betweeness
bow1 = net.balanced_tree(2,1)
bow2 = net.balanced_tree(2,1)
bow3 = net.disjoint_union(bow1,bow2)
bow3.add_node(6)
niter=bow3.nbunch_iter([0,1,2,3,4,5])
for node in niter:
    bow3.add_edge(6,node)
bow3.add_edges_from([(1,2),(4,5)] )
net.draw(bow3)
plot.show()
net.betweenness_centrality(bow3)

#3b. On russion graph
b=net.betweenness_centrality(core10)
bs=sorted_map(b)
bs[:10]



#4. Centrality Summary

## make a list of the elite group by merging top ten groups for 3 centrality metrics
names1=[x[0] for x in ds[:10]]
names2=[x[0] for x in cs[:10]]
names3=[x[0] for x in bs[:10]]

## use Python sets to compute a union of the sets
names=list(set(names1) | set(names2) | set (names3))

b = dict((x,y) for x,y in bs[:] )
c = dict((x,y) for x,y in cs[:] )
d = dict((x,y) for x,y in ds[:] )
## build a table with centralities
table=[[name,d[name],c[name],b[name]] for name in names]


### Gray Cardinal, note slightly different then book..

singleG = net.convert.to_networkx_graph(g)
core10G=trim_degrees(singleG,degree=10)
grey_cardinal = net.eigenvector_centrality(core10G)
gcs=sorted_map(grey_cardinal)
print gcs[:20]


### Page Rank
directed = net.DiGraph()
net.convert.to_networkx_graph(g,directed)
core10directed=trim_degrees(directed,degree=10)
pr=net.pagerank(core10directed)
prs=sorted_map(pr)
print prs[:20]
