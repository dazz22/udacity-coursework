# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]
# import time
# import multiprocessing


def find_eulerian_tour(graph):
        # your code here
    return []


graph = [
    (8, 16), (8, 18), (16, 17), (18, 19), (3, 17), (13, 17), (5, 13), (3, 4),
    (0, 18), (3, 14), (11, 14), (1, 8), (1, 9), (4, 12), (2, 19), (1, 10),
    (7, 9), (13, 15), (6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15),
    (8, 13), (10, 17)
]

graph = [(1, 2), (2, 3), (3, 1)]


def findmatch(graph2, lstnode, lengraph):
    for a in range(0, lengraph):
        if graph2[a][0] == lstnode:
            lstnode = graph2[a][1]
            return [a, lstnode]

        elif graph2[a][1] == lstnode:
            lstnode = graph2[a][0]
            return [a, lstnode]

    return [-1, lstnode]


def test(graph):
    a = 0
    lengraph = len(graph)
    tour = []
    lstnode = min(graph)[0]
    b = graph.index(min(graph))
    print(b)
    tour.append(lstnode)
    while a != -1:
        [a, lstnode] = findmatch(graph, lstnode, lengraph)
        if a != -1:
            tour.append(lstnode)

    print(tour)
    return tour

# p = multiprocessing.Process(target=test, name="TEST", args=graph)
# p.start()
# p.join(20)
# for line in iter(p.stdout.readline, b''):
#    print(line)
# p.terminate()


print(graph)
test(graph)
# print(min(graph)[0])
