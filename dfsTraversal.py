# iterative
def dfsTraversalWeHave(graph, startingNode):
    stack = [startingNode]
    res = ""
    while len(stack) > 0:
        top = stack.pop()
        res += top
        for neighbour in graph[top]:
            stack.append(neighbour)
    return res

def dfsTraversalRecursive(graph , startingNode):
    res = ""

    res+= startingNode

    for neighbour in graph[startingNode]:
        res += dfsTraversalRecursive(graph , neighbour)

    return res
graph = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}
print(dfsTraversalWeHave(graph, "a"))
print(dfsTraversalRecursive(graph , "a"))
