edges = [
    ["i", "j"],
    ["k", "i"],
    ["m", "k"],
    ["k", "l"],
    ["o", "n"]
]
def buildGraph(edges):
    graph = {}
    for edge in edges:
        a = edge[0]
        b = edge[1]
        if a not in graph:
            graph[a] = []
        if b not in graph :
            graph[b] = []
        graph[a]+=b
        graph[b]+=a
    return graph


def checkPath(graph, src, des, visited):

    if src == des:
        return True
    if src in visited:
        return False
    visited.add(src)

    for neighbour in graph[src]:
        if checkPath(graph, neighbour, des, visited):
            return True
    else:
        return False


def undirectedPathWithCycle(edges, source, destination):
    graph = buildGraph(edges)
    return checkPath(graph , source , destination , visited = set())


print(undirectedPathWithCycle(edges , source = "i" , destination = "n"))
