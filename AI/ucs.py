# -*- coding: utf-8 -*-
"""
@author: 20pw39
"""
import networkx as nx
import matplotlib.pyplot as plt

g = {
    5: {3: 1, 8 :6},
    3: {2: 3, 4: 1},
    2: {},
    4: {8: 1},
    8: {9: 4}
}

for key, dVal in g.items():
    for i in dVal:
        dVal[i] = {'weight': dVal[i]}
        
print(g)        

def uniformCost(g, start, dest):
    vis=set()
    q=list()
    path = [start]
    q.append([0, path])
    
    while q:
        q.sort()
        dis,path = q.pop(0)        
        s =path[len(path)-1]
        if s==dest:
            return [path, dis]
        vis.add(s)
        
        for n in g[s].keys():
            if n not in vis:
                travPath=list(path)
                travPath.append(n)
                q.append([dis + g[s][n]['weight'] , travPath])

G = nx.DiGraph(g)
pos = nx.spring_layout(G,k=.8)
nx.draw_networkx(G, pos)

labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()

start=5
dest=9

print(uniformCost(g,start,dest))