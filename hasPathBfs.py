

def findPathBfs(graph , source , destination):

    queue = [source]

    while(len(queue) > 0 ):
        front = queue.pop(0)

        for neighbour in graph[front]:
            queue.append(neighbour)
            if neighbour == destination:
                return True
    return False

graph = {
    "f": ["g", "i"],
    "g": ["h"],
    "h": [],
    "i": ["g", "k"],
    "j": ["i"],
    "k": []
}

print(findPathBfs(graph , source= "f" , destination = "j"))