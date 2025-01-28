from points import Point

# Iloczyn wektorowy
def cross_product(ref: Point, p1: Point, p2: Point):
    return (p1.x - ref.x) * (p2.y - ref.y) - (p1.y - ref.y) * (p2.x - ref.x)

# Funkcja porównująca punkty, który jest na lewo, a który na prawo od punktu odniesienia.
def compare(min_y_point, p1, p2):
    if p1 == min_y_point:
        return 1
    if p2 == min_y_point:
        return -1

    area = cross_product(min_y_point, p1, p2)

    if area < 0:
        return -1
    if area > 0:
        return 1
    if area == 0:
        if p1.x == p2.x:
            return 1 if p1.y < p2.y else -1
        else:
            return 1 if p1.x < p2.x else -1


# Funkcja jak powyżej z drobną modifikacja
def short_compare(min_y_point, p1, p2):
    if p1 == min_y_point:
        return 1
    if p2 == min_y_point:
        return -1

    area = cross_product(min_y_point, p1, p2)

    if area < 0:
        return -1
    if area > 0:
        return 1
    if area == 0:
        return 1

