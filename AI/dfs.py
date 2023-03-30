import networkx as nx
import matplotlib.pyplot as plt


def dfsTraversal(graph, node, vis, dest):
    path.append(node)
    if node == dest:
        return True
    vis.add(node)

    for i in graph[node]:
        if i not in vis:
            if dfsTraversal(graph, i, vis, dest):
                return True
            else:
                path.pop()
    return False
                   
graph = {
    '1': ['3', '8'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': ['9']
}


G = nx.DiGraph(graph)
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos)

start = '1'
dest = '9'
path = list()
vis = set()

dfsTraversal(graph, start, vis, dest)

print(path)
   
path_edges = []

for i in range(len(path)-1):
    path_edges.append([path[i], path[i+1]])

nx.draw_networkx_edges(G,pos,edgelist=path_edges,edge_color='g',width=2)
plt.show()
