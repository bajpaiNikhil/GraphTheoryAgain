

def breadthFirstTraversal(graph , startingNode):

    queue = [startingNode]
    res = ""
    while len(queue)>0:
        top =  queue.pop(0)
        res+=top
        for neighbour in graph[top]:
            queue.append(neighbour)

    return (res)

graph = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

print(breadthFirstTraversal(graph , "a"))