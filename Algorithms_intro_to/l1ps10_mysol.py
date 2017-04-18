# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]


def find_eulerian_tour(graph):
    a = 0
    graph2 = graph
    tour = []
    tour2 = []
    while len(graph2) > 0:
        [tour, graph2] = onetour(graph2, a)
        for b in range(0, len(tour2)):
            if tour2[b] == tour[0]:
                tour2[b:b+1] = tour
                tour = [-1]
        if len(tour2) == 0:
            tour2 = tour

    return tour2


def onetour(graph, a):

    tour = []
    tour.append(graph[a][0])
    lstnode = graph[a][1]
    graph.remove(graph[a])
    tour.append(lstnode)
    while a != -1:
        [a, lstnode] = nextnode(graph, lstnode, tour)
        if a != -1:
            tour.append(lstnode)
            if len(graph) > 0:
                graph.remove(graph[a])

    return [tour, graph]


def nextnode(graph, lstnode, tour):
    lstnodet = lstnode
    at = 0
    for a in range(0, len(graph)):
        if graph[a][0] == lstnode:
            at = a
            lstnodet = graph[a][1]

        elif graph[a][1] == lstnode:
            at = a
            lstnodet = graph[a][0]

        if(lstnodet not in tour):
            return [at, lstnodet]

    if lstnodet != lstnode:
        return [at, lstnodet]

    return [-1, lstnode]

graph = [
        (0, 1), (1, 5), (1, 7), (4, 5),
        (4, 8), (1, 6), (3, 7), (5, 9),
        (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)
]

print(find_eulerian_tour(graph))
