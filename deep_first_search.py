def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbour)

def dfs_(graph, node):
    visited = set()
    dfs(visited, graph, node)
