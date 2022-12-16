def closestPoint(points, k):
    distance = []
    cor = []

    for point in points:
        result = (pow(point[0], 2) + pow(point[1], 2))
        distance.append(result)

    unsorted = distance.copy()
    distance.sort()

    result = [distance[i] for i in range(k)]
    for i in result:
        cor.append(unsorted.index(i))    
    result = [points[i] for i in cor]

    return result

closestPoint([[3,3],[5,-1],[-2,4]], 2)