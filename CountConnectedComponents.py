graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2],
}


def explore(graph, currentNode , visited):
    if currentNode in visited:
        return False
    visited.add(currentNode)
    for neighbour in graph[currentNode]:
        explore(graph , neighbour , visited)
    return True

def traverseGraphNode(graph):
    visited = set()
    count = 0
    for node in graph:
        if explore(graph , node , visited):
            count+=1
    return count

print(traverseGraphNode(graph))