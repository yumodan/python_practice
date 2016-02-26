import queue
"""given an adjacency list representation of an undirected graph implement a bfs traversal
  bfs_select will return a list of tuples. the 0 index of the tuple will contain the node/vertex
  traveled to and the 1 index of the tuple will contain the length from the starting node
"""

def bfs_select(graph, start):
    result = []
    Q = queue.Queue()
    Q.put((start, 0))
    visited = visits(graph)
    visited[start] = (True, 0)
    while not Q.empty():
        start = Q.get()
        frontier = start[1]
        start = start[0]
        for edge in graph[start]:
            if not visited[edge][0]:
                Q.put((edge, frontier + 1))
                visited[edge] = (True, frontier + 1)
    for vertex in visited:
        if visited[vertex][0]:
            result.append((vertex, visited[vertex][1]))
    return result


def visits(graph):
    visited = {}
    for vertex in graph:
        visited[vertex] = (False, 0)
    return visited

# undirected graph below
g = {
  "a": ["b", "d"],
  "b": ["d", "a"],
  "c": ["d", "e", "f"],
  "d": ["a", "b", "c"],
  "e": ["c"],
  "f": ["c"]
}
# print(visits(g))
print(bfs_select(g, "b"))