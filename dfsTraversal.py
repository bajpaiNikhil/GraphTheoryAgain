
def dfsTraversalWeHave(graph, startingNode):
    stack = [startingNode]
    res = ""
    while len(stack) > 0:
        top = stack.pop()
        res += top
        for neighbour in graph[top]:
            stack.extend(neighbour)
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
