# -*- coding: utf-8 -*-
"""
@author: 20pw39
"""

import queue as Q

graph = {'a': [('b', 2), ('c', 2)],
          'b': [('a', 2), ('d', 1)],
          'c': [('a', 2), ('d', 8), ('f', 3)],
          'd': [('b', 1), ('c', 8), ('e', 2), ('S', 3)],
          'e': [('d', 2,), ('h', 8), ('r', 2), ('S', 9)],
          'f': [('c', 3), ('G', 2), ('r', 2)],
          'G': [('f', 2)],
          'h': [('e', 8), ('p', 4), ('q', 4)],
          'p': [('h', 4), ('q', 15), ('S', 1)],
          'q': [('h', 4), ('p', 15)],
          'r': [('e', 2), ('f', 2)],
          'S': [('d', 3), ('e', 9), ('p', 1)]}

hVal = {'S': 0, 'a': 5, 'b': 7, 'c': 4, 'd': 7, 'e': 5, 'f': 2, 'G': 0, 'h':11, 'p': 14, 'q': 12, 'r': 3}

def aStarAlgo(graph, start, dest):
    vis = []
    path = []
    prev = {}
    queue = Q.PriorityQueue()
    queue.put((0, start, None))
    h2= 0
    while queue:
        cost, node, prev_n = queue.get()
        if node not in vis:
            vis.append(node)
            prev[node] = prev_n
            if node == dest:               
                while prev[node] != None:
                    path += [node]
                    node = prev[node]
                path += [start]   
                return vis, prev, path[::-1]
            for i, c in graph[node]:
                if i not in vis:
                    totalCost = cost + c
                    h1 = hVal[i]
                    total = totalCost + h1 - hVal[node]
                    queue.put((total, i, node))


vis, prev, path = (aStarAlgo(graph, 'S', 'G'))
print("The vis nodes are:")
print(vis)

print("\n The path followed is:")
print(path)

print("\n list of previous nodes:")
print(prev)