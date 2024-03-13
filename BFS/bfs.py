# represent graph
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

# function to travarse the graph using BFS
def bfs(graph, node):
    visited = []
    q = []
    visited.append(node)
    q.append(node)
    while q :
        n = q.pop(0)
        print(n, end=" ")
        for neighbour in graph[n]:
            if neighbour not in visited:
                visited.append(neighbour)
                q.append(neighbour)
    
bfs(graph,'5')

# time complexity O(V+E)
# space complexity O(V)