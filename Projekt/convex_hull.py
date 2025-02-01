from heap import heap_sort
from compare import compare, short_compare


# GRAHAM SCAN ALGORITHM

# Funkcja zwraca punkt o najmniejszej wartości współrzędnej y.
# W przypadku, gdy istnieje więcej niż jeden punkt o tej samej wartości y,
# wybierany jest punkt o najmniejszej współrzędnej x.
def get_min_y(list_points):
    point_min_y = list_points[0]

    for point in list_points[1:]:
        if point_min_y.y > point.y:
            point_min_y = point
        elif point_min_y.y == point.y:
            if point_min_y.x > point.x:
                point_min_y = point
    return point_min_y


# Fynkcja sortuje punkty ze wzgeldu na kąt jaki tworzą z osia x oraz punktem min_y
def sort_by_angle(list_points, point_min_y):
    heap_sort(list_points, point_min_y)

# Funkcja wyznacza punkty, które tworzą convex hull
def convex_hull(points):

    length = len(points)
    point_min_y = get_min_y(points)
    sort_by_angle(points, point_min_y)
    print(points)
    if length < 3:
        points.reverse()
        return points

    stack = [points[length - 1], points[length - 2]]

    for i in range(length - 3, -1, -1):
        next_point = points[i]
        point = stack.pop()
        while stack and short_compare(stack[-1], point, next_point) == -1:
            point = stack.pop()
        stack.append(point)
        stack.append(next_point)


    for i in range(1, length - 1, 1):
        if points[i].x != stack[-1].x or points[i] == point_min_y or points[i] == stack[-1]:
            break
        stack.append(points[i])

    return stack
