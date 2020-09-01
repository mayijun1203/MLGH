import networkx as nx
import pandas as pd



gu=nx.Graph()
gu.add_edge('A','B')


gd=nx.DiGraph()
gd.add_edge('A','B')


gw=nx.Graph()
gw.add_edge('A','B',weigth=6)


gs=nx.Graph()
gs.add_edge('A','B',sign='+')



gs=nx.MultiGraph()
gs.add_edge('A','B',relation='friend')
gs.add_edge('A','B',relation='neighbor')
gs.add_node('A',role='trader')




gb=nx.Graph()
gb.add_nodes_from(['A','B','C','D'],bipartite=0)
gb.add_nodes_from(['1','2','3','4'],bipartite=1)







g=nx.Graph()
g.add_edges_from([(0,1),(0,2),(0,3),(0,5),(1,3),(1,6),(3,4),(4,5),(4,7),(5,8),(8,9)])
nx.draw_networkx(g)

# Local Clustering Coefficient: 1/(4*3/2)
nx.clustering(g,0)

# Global Clustering Coefficient
nx.average_clustering(g)

# Transitivity (3*closed triads/open triads)
nx.transitivity(g)

# Path
nx.shortest_path(g,0,7)
nx.shortest_path_length(g,0,7)
nx.shortest_path_length(g,0)
nx.average_shortest_path_length(g)
nx.diameter(g) # longest path length
nx.eccentricity(g) # longest path length for each node
nx.radius(g) # min eccentricity
nx.periphery(g) # nodes with eccentricity=diameter
nx.center(g) # nodes with eccentricity=radius

nx.bfs_tree(g,0).edges()


# Connectivity
nx.is_connected(g)
sorted(nx.connected_components(g))
nx.node_connectivity(g)
nx.minimum_node_cut(g)
nx.edge_connectivity(g)
nx.minimum_edge_cut(g)
nx.minimum_node_cut(g,4,0)
nx.minimum_edge_cut(g,4,0)




# Centrality
nx.degree_centrality(g) # degree/number of nodes
nx.closeness_centrality(g) # number of nodes/sum of shortest path lengths
nx.betweenness_centrality(g,normalized=True,endpoints=False,k=5) # sum of (# of shortest path through the node/# of shortest paths)
nx.edge_betweenness_centrality(g,normalized=True) # sum of (# of shortest path through the edge/# of shortest paths)








# Karate Club Data
k=nx.karate_club_graph()
nx.draw_networkx(k,pos=nx.random_layout(k))
nx.draw_networkx(k,pos=nx.circular_layout(k))
nx.draw_networkx(k,pos=nx.circular_layout(k),edge_color='0.4',alpha=0.1)



# Page Rank
# Assuming equal share at the beginning and recalculate based on the share received till convergence
nx.pagerank(g)
# Scaled Page Rank with Random Walker
nx.pagerank(g,alpha=0.8)



# Hubs and Authorities
# Auth score as in degrees
# Hub score as out degrees
nx.hits(g)





# Preferential Attachment Model
# degree of the node/sum of degrees of all nodes
g=nx.barabasi_albert_graph(1000000,1)
d=g.degree()
h=pd.DataFrame(d)[1].hist(bins=1000,log=True)




# Small World Model
# Start with a ring and begin to rewire the edges randomly
g=nx.watts_strogatz_graph(100,6,0.04)
nx.draw_networkx(g)
d=g.degree()
h=pd.DataFrame(d)[1].hist()
nx.average_clustering(g)
nx.average_shortest_path_length(g)
# Connected Small World Network (run Watts up to t times till it returns a connected network)
g=nx.connected_watts_strogatz_graph(100,6,0.04,50)
nx.draw_networkx(g)
# Newman Watts (adding new edges instead of rewiring)
g=nx.newman_watts_strogatz_graph(100,6,0.04)
nx.draw_networkx(g)




# Link Prediction
# Common Neighbors
cn=[(x[0],x[1],len(list(nx.common_neighbors(g,x[0],x[1])))) for x in nx.non_edges(g)]
# Jaccard Coefficient (# of common neighbors/total neighbors)
jc=list(nx.jaccard_coefficient(g))
# Resources Allocation (sum of fractions of the end node receive from middle nodes based on their degrees)
ra=list(nx.resource_allocation_index(g))
# Adamic-Adar Index (Resources Allocation with log of degrees)
aa=list(nx.adamic_adar_index(g))
# Preferential Attachment (product of nodes' degree)
pa=list(nx.preferential_attachment(g))
# Community Common Neighbors (with bonus for nieghbors in the same community)
g.nodes[0]['community']=0
g.nodes[1]['community']=1
g.nodes[2]['community']=0
g.nodes[3]['community']=1
g.nodes[4]['community']=1
g.nodes[5]['community']=0
g.nodes[6]['community']=1
g.nodes[7]['community']=1
g.nodes[8]['community']=0
g.nodes[9]['community']=0
ccn=list(nx.cn_soundarajan_hopcroft(g))
# Community Resource Allocation (only consider nodes in the same community)
g.nodes[0]['community']=0
g.nodes[1]['community']=1
g.nodes[2]['community']=0
g.nodes[3]['community']=1
g.nodes[4]['community']=1
g.nodes[5]['community']=0
g.nodes[6]['community']=1
g.nodes[7]['community']=1
g.nodes[8]['community']=0
g.nodes[9]['community']=0
cra=list(nx.ra_index_soundarajan_hopcroft(g))


