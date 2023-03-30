# -*- coding: utf-8 -*-
h = {
     0: 9,
     1: 7,
     2: 5,
     3: 1,
     4: 7,
     5: 0
    }

G = {
     0: {1:2, 4:2 },
     1: {0:2 , 2:2 , 4:2 },
     2: {1:2 , 3:4 },
     3: {2:4 , 4:6 , 5:1 },
     4: {0:2, 1:2, 3:6 },
     5: {3:1 }
    }

def a_star(G, h, start, goal):
    q = []
    q.append((h[0], [start], 0))
    visited = set()
    
    while q:
        q.sort()
        
        f = q[0][0]
        i = 0
        while i<len(q) and q[i][0]==f:
            visited.add(q[i][1][-1])
            i+=1
            
        j=0
        while q and q[j][0]==f:
            f, path, g = q.pop(0)
            node = path[len(path)-1]
            
            if node==goal:
                return [path, g]
            
            for i in G[node].keys():
                if i not in visited:
                    new_path= list(path)
                    new_path.append(i)
                    q.append((h[i]+g+G[node][i], new_path, g+G[node][i]))
            j+=1
            
print(a_star(G, h, 0, 5))