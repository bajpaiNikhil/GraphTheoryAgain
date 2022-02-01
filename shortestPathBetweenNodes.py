edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]


def convertToGraph(edges):
    graph = {}
    for node in edges:
        a = node[0]
        b = node[1]
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a] += b
        graph[b] += a
    return graph


def shortestPath(edges, starting, destinatoin):

    graph = convertToGraph(edges)
    queue = [[starting, 0]]
    visited = set(starting)

    while len(queue) > 0:
        top = queue.pop(0)

        # print(top, visited, top[0], top[1] )
        if top[0] == destinatoin:
            return top[1]
        for neighbour in graph[top[0]]:

            if neighbour not in visited:
                visited.add(neighbour)
                queue.append([neighbour, top[1] + 1])
    return -1


print(shortestPath(edges, starting='w', destinatoin='z'))
