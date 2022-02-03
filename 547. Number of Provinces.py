isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# def explore(isConnected, r, c, visited):
#     rowInBound = 0 <= r < len(isConnected)
#     colInBound = 0 <= c < len(isConnected[0])
#
#     if not rowInBound or not colInBound:
#         return False
#     position = str(r) + "," + str(c)
#     if position in visited:
#         return False
#     visited.add(position)
#     print(visited)
#     if isConnected[r][c] == 0:
#         return False
#
#     explore(isConnected, r - 1, c, visited)
#     explore(isConnected, r + 1, c, visited)
#     explore(isConnected, r, c - 1, visited)
#     explore(isConnected, r, c + 1, visited)
#     return True
#
#
# count = 0
# for i in range(len(isConnected)):
#     for j in range(len(isConnected[0])):
#         if explore(isConnected, i, j, visited):
#             count += 1
#
# print(count)


from collections import defaultdict
def fromAjdMatrixToAdjList(isConnected):
    graph = defaultdict(list)
    for i in range(len(isConnected)):
        for j in range(len(isConnected[0])):
            if isConnected[i][j] == 1:
                graph[i].append(j)
    return dict(graph)


def exploreConnectedComponent(graph , node, visited):
    if node in visited:
        return False
    visited.add(node)

    for neighbour in graph[node]:
        exploreConnectedComponent(graph , neighbour , visited)
    return True


def exploreAjdList(isConnected):
    count = 0
    graph= fromAjdMatrixToAdjList(isConnected)
    visited = set()
    for node in graph:
        if exploreConnectedComponent(graph , node , visited):
            count+=1
    return count



print(exploreAjdList(isConnected))