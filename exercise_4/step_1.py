import numpy as np


def perimeter(points):
    if len(points) < 3:
        return 0

    dists = []

    points_round = points + [points[0]]
    for i in range(len(points)):
        p1 = np.array(points_round[i])
        p2 = np.array(points_round[i+1])
        dists.append(np.linalg.norm(p1 - p2))

    return sum(dists)
