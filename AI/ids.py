# -*- coding: utf-8 -*-
"""
@author: 20pw39
"""
import networkx as nx
import matplotlib.pyplot as plt
graph = {
    '1': ['3', '8'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': ['9']
}
def iterDeep(start, dest, levelLimit, begin=0):
    for x in range(begin, levelLimit+1):
        path = list()
        vis = set()
        if(depthLimited(start, dest, vis, path, 0, x)):
            return [path, True]
    return [[], False]
    

def depthLimited(node, dest, vis, path, depth, L):
    path.append(node)
    if node == dest:
        return True
    for i in graph[node]:
        if depth<L:
            vis.add(node)
            if i not in vis:
                if depthLimited(i, dest, vis, path, depth+1, L):
                    return True
                else:
                    path.pop()
        else:
            return False
    return False

start = '1'
dest = '8'
print(iterDeep(start, dest, 5))
