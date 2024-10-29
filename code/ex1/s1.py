import math


def euklides_distance(point1: list, point2: list):
    """ Points as lists [x, y, z] """
    return math.sqrt(
        (point1[0] - point2[0]) ** 2 +
        (point1[1] - point2[1]) ** 2 +
        (point1[2] - point2[2]) ** 2
    )


point1 = [1, 2, 3]
point2 = [4, 6, 8]

distance = euklides_distance(point1, point2)
print(distance)
