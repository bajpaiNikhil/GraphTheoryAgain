

def findPathBfs(graph , source , destination):

    queue = [source]

    while(len(queue) > 0 ):
        front = queue.pop(0)
        if front == destination:
            return True
        for neighbour in graph[front]:
            queue.append(neighbour)
    return False

graph = {
    "f": ["g", "i"],
    "g": ["h"],
    "h": [],
    "i": ["g", "k"],
    "j": ["i"],
    "k": []
}

print(findPathBfs(graph , source= "f" , destination = "f"))