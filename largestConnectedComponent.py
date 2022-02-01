

graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2],
}

def exploreSize(graph , currentNode , visited ):
    if currentNode in visited :
        return 0
    visited.add(currentNode)
    size = 1
    for neighbour in graph[currentNode]:
        size +=exploreSize(graph, neighbour, visited )
    return size

def sizeOfLargestComponent(graph):
    visited = set()
    largest = 0
    for node in graph:
        largest = max(exploreSize(graph , node , visited) , largest)

    return largest

print(sizeOfLargestComponent(graph))




