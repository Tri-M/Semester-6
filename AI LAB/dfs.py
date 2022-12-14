graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

vis=set()

def dfs(vis,graph,node):
    if node not in vis:
        print(node)
        vis.add(node)
        for neigh in graph[node]:
            dfs(vis,graph,neigh)
            
dfs(vis,graph,'5')
