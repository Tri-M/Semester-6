import networkx as nx
import matplotlib.pyplot as plt
class GraphVis:
    def __init__(self):
        self.visual=[]
    
    def addEdge(self,a,b):
        tem=[a,b]
        self.visual.append(tem)
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

vis=[]
q=[]

def bfs(vis,graph,node,goal):
    vis.append(node)
    q.append(node)
    
    while q:
        n=q.pop(0)
        print(n,end="")
        for neigh in graph[n]:
            if neigh not in vis:
                vis.append(neigh)
                q.append(neigh)
                if neigh==goal:
                    return
bfs(vis,graph,'5','7')
print(vis)

G=GraphVis()
for i,j in graph.items():
    for k in j:
        G.addEdge(i, k)
G.visualize()