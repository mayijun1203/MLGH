import networkx as nx



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
















