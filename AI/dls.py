import networkx as nx
import matplotlib.pyplot as plt

def depthLimited(graph, node, vis,dest, depth, L):
    path.append(node)
    if node ==dest:
        return True
    for i in graph[node]:

        if depth<L:
            vis.add(node)
            if i not in vis:
                if depthLimited(graph, i, vis,dest, depth+1, L):
                    return True
                else:
                    path.pop()
        else:
            return False

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
dest = '8'

path = list()
vis = set()

print(depthLimited(graph, start, vis,dest, 0, 1))

print(path)
   
path_edges = []

for i in range(len(path)-1):
    path_edges.append([path[i], path[i+1]])

nx.draw_networkx_edges(G,pos,edgelist=path_edges,edge_color='g',width=2)
plt.show()
