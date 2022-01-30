# given the graph find weather there is a path between source and destination
graph = {
    "f": ["g", "i"],
    "g": ["h"],
    "h": [],
    "i": ["g", "k"],
    "j": ["i"],
    "k": []
}


def findPathIterative(graph, source, destination):
    stack = [source]
    res = ""
    while len(stack) > 0:
        top = stack.pop()
        if top == destination:
            return True
        res += top
        for neighbour in graph[top]:
            stack.append(neighbour)
    return False

def findPathRecursive(graph , source , destination):

    if source == destination:
        return True
    for neighbour in graph[source]:
        return findPathRecursive(graph , neighbour , destination)

print(findPathIterative(graph, "f", "f"))
print(findPathRecursive(graph , "f" , "f"))
