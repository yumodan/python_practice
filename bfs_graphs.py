import queue
"""given an adjacency list representation of an undirected graph implement a bfs traversal"""

def bfs_select(graph, start):
    Q = queue.Queue()
    visited = visits(graph)
    Q.put(start)
    visited[start] = True
    while not Q.empty():
        start = Q.get()
        for edge in graph[start]:
            if not visited[edge]:
                Q.put(edge)
                visited[edge] = True
    result = []
    for vertex in visited:
        if visited[vertex]:
            result.append(vertex)
    return result
        

def visits(graph):
    visited = {}
    for vertex in graph:
        visited[vertex] = False
    return visited


g = {
  "a": ["b", "d"],
  "b": ["d", "a"],
  "c": ["d"],
  "d": ["a", "b", "c"]
}
print(visits(g))
print(bfs_select(g, "b"))