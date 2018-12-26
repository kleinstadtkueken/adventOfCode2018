#!/usr/bin/python3

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y', 'z', 't'])


filename = 'input.txt'
# filename = 'example1.txt' # --> 4


def distance(p1: Point, p2: Point):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y) + abs(p1.z - p2.z) + abs(p1.t - p2.t)




points = []

with open(filename, 'r') as file:
    for line in file:
        coordinate = line[:-1].split(',')
        points.append(Point(int(coordinate[0]), int(coordinate[1]), int(coordinate[2]), int(coordinate[3])))



clusters = []

for i in range(len(points) - 1):
    current = points[i]
    cluster = {current}
    for j in range(i + 1, len(points)):
        comp = points[j]

        if distance(current, comp) <= 3:
            cluster.add(comp)

    clustersToCombine = []
    for aCluster in clusters:
        if len(aCluster & cluster) > 0:
            clustersToCombine.append(aCluster)

    if len(clustersToCombine) == 0:
        clusters.append(cluster)
    elif len(clustersToCombine) == 1:
        clustersToCombine[0].update(cluster)
    else:
        clusters.append(cluster)
        for c in clustersToCombine:
            cluster.update(c)

            clusters.remove(c)


print(len(clusters))

