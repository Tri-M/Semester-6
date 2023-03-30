import networkx as nx
import matplotlib.pyplot as plt

def bfsGraph(graph, start, dest):   
    vis = set()
    queue = list()
    path = list()

    path.append(start)
    queue.append(path)
   
    while len(queue):
        path = queue.pop(0)
        s = path[len(path)-1]

        if s == dest:
            return path

        vis.add(s)
        for i in graph[s]:
            if i not in vis:
                travPath = list(path)
                travPath.append(i)
                queue.append(travPath)
    return []
                   
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

path = bfsGraph(graph, start, dest)

print(path)

pathEdges = [[path[i], path[i+1]] for i in range(len(path)-1)]

nx.draw_networkx_edges(G, pos, edgelist=pathEdges, edge_color='g', width=2)
plt.show()


