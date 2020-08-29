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
