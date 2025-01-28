import math

# Funkcja oblicza dystans
def distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)


# Funkcja zwraca punkt z najwiekszym y oraz x
def get_max_y(list_points):
    point_min_y = list_points[0]
    for point in list_points[1:]:
        if point_min_y.y < point.y:
            point_min_y = point
        elif point_min_y.y == point.y:
            if point_min_y.x < point.x:
                point_min_y = point
    return point_min_y


# Funkcja zwraca stosunek y/x
def yx(p1, p2):
    x = abs(p1.x - p2.x)
    y = abs(p1.y - p2.y)

    return 0 if x == 0 or y == 0 else y/x

# Funkcja zwraca kąt w stopniach
def degree(p1, p2, flag):
    angle = math.degrees(math.atan(yx(p1, p2)))
    if flag:
        return angle if p1.x <= p2.x else 180 - angle
    else:
        return angle if p1.x >= p2.x else 180 - angle


# Funkcja wylicza dystans przeciwleglych punktow
def rotating_calipers(points):

    result = []
    n = len(points)

    max_y_point = get_max_y(points)
    min_y_point = points[0]

    top_point = max_y_point
    bottom_point = min_y_point

    top_index = points.index(max_y_point)
    bottom_index = 0

    dist = distance(max_y_point, min_y_point)
    result = [dist, max_y_point, min_y_point]

    previous_top_agnle = 0
    previous_bottom_agnle = 0

    bottom_index = bottom_index + 1
    top_index = (top_index + 1) % n
    next_bottom_point = points[bottom_index]
    next_top_point = points[top_index]

    top_angle = degree(top_point, next_top_point, 0)
    bottom_angle = degree(bottom_point, next_bottom_point, 1)

    while top_point != min_y_point and bottom_point != max_y_point:

        while bottom_angle == previous_bottom_agnle and bottom_point != max_y_point:
            bottom_index = bottom_index + 1
            bottom_point = next_bottom_point
            if bottom_index >= n:
                break
            next_bottom_point = points[bottom_index]
            previous_bottom_agnle = bottom_angle
            bottom_angle = degree(bottom_point, next_bottom_point, 1)


        while top_angle == previous_top_agnle and top_point != min_y_point:
            top_index = (top_index + 1) % n
            top_point = next_top_point
            next_top_point = points[top_index]
            previous_top_agnle = top_angle
            top_angle = degree(top_point, next_top_point, 0)


        dist = distance(bottom_point, top_point)

        if dist > result[0]:
            result.clear()
            result = [dist, top_point, bottom_point]

        if bottom_angle < top_angle and bottom_point != max_y_point:
            bottom_index = bottom_index + 1
            bottom_point = next_bottom_point
            if bottom_index >= n:
                break
            next_bottom_point = points[bottom_index]
            previous_bottom_agnle = bottom_angle

            dist = distance(bottom_point, top_point)
            if dist > result[0]:
                result.clear()
                result = [dist, top_point, bottom_point]

            bottom_angle = degree(bottom_point, next_bottom_point, 1)

        dist = distance(bottom_point, top_point)

        if dist > result[0]:
            result.clear()
            result = [dist, top_point, bottom_point]

        if bottom_angle > top_angle and top_point != min_y_point:
            top_index = (top_index + 1) % n
            top_point = next_top_point
            next_top_point = points[top_index]
            previous_top_agnle = top_angle
            dist = distance(bottom_point, top_point)
            if dist > result[0]:
                result.clear()
                result = [dist, top_point, bottom_point]

            top_angle = degree(top_point, next_top_point, 0)

        dist = distance(bottom_point, top_point)

        if dist > result[0]:
            result.clear()
            result = [dist, top_point, bottom_point]

        if top_angle == bottom_angle:
            top_index = (top_index + 1) % n
            top_point = next_top_point
            next_top_point = points[top_index]
            previous_top_agnle = top_angle

            bottom_index = bottom_index + 1
            bottom_point = next_bottom_point
            next_bottom_point = points[bottom_index]
            previous_bottom_agnle = bottom_angle

            top_angle = degree(top_point, next_top_point, 0)
            bottom_angle = degree(bottom_point, next_bottom_point, 1)

    return result


