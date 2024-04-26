import math

points = [(2,3),(4,5),(1,7),(4,4),(2,9)]


def euclideanDistance(x,y):
    x1,x2 = x
    y1,y2 = y
    result = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    return result

distances = []


for i in range(len(points)):
    for j in range(i+1,len(points)):
        distance = euclideanDistance(points[i],points[j])
        distances.append(distance)


min_distance = min(distances)
print(min_distance)