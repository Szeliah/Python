#JEZYK PYTHON
#GRUPA CWICZENIOWA 02
#Zadania z zajec z dnia 27.11.2024
#Autor: Szymon Szeliga

from points import Point
from math import pi as PI
from math import sqrt



class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):        # "Circle(x, y, radius)"
        return f"Circle({self.pt.x}, {self.pt.y}, {self.radius})"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):           # pole powierzchni
        return PI * self.radius * self.radius

    def move(self, x, y):     # przesuniecie o (x, y)
        self.pt.x = self.pt.x + x
        self.pt.y = self.pt.y + y

    def cover(self, other):   # najmniejszy okrąg pokrywający oba
        x1 = self.pt.x
        y1 = self.pt.y
        r1 = self.radius

        x2 = other.pt.x
        y2 = other.pt.y
        r2 = other.radius

        if r1 > r2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            r1, r2 = r2, r1

        distance = sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

        #Czy mniejszy okrag znajduje się cały w okregu wiekszym
        if r1 + distance <= r2:
            return Circle(x2, y2, r2)
        else:
            r3 = (distance + r1 + r2) / 2
            factor = 0.5 + (r2 - r1) / (2 * distance)
            x3 = (1 - factor) * x1 + factor * x2
            y3 = (1 - factor) * y1 + factor * y2
            return Circle(x3, y3, r3)


    #Użyłem tej metody:
    #Cartesian coordinates from cross- and dot-products
    #https://en.wikipedia.org/wiki/Circumcircle

    @classmethod
    # Sprawdzenie czy punkty NIE są wspóliniowe
    def is_non_collinear_points(cls, pt1, pt2, pt3):
        a_vector = Point(pt1.x - pt2.x, pt1.y - pt2.y)
        b_vector = Point(pt2.x - pt3.x, pt2.y - pt3.y)
        return a_vector.cross(b_vector) != 0

    @classmethod
    def from_points(cls, points):
        if len(points) is not 3 and not cls.is_non_collinear_points(points[0], points[1], points[2]):
            raise ValueError("Bledna ilosc danych lub punkty są wspóliniowe")

        P1, P2, P3 = points

        # Czynniki dla alfy
        P4 = P2 - P3
        P4P4 = P4 * P4
        P5 = P1 - P2
        P6 = P1 - P3
        P7 = P2 - P3
        P8 = P5.cross(P7)
        P5P6 = P5 * P6

        denominator = 2 * (P8 * P8)

        alfa = (P4P4 * P5P6) / denominator

        # Czynniki dla bety
        P6P6 = P6 * P6
        P9 = P2 - P1
        P9P7 = P9 * P7

        beta = (P6P6 * P9P7) / denominator

        # Czynniki dla gammy
        P5P5 = P5 * P5
        P10 = P3 - P1
        P11 = P3 - P2
        P10P11 = P10 * P11

        gamma = (P5P5 * P10P11) / denominator

        centre_x = P1.x * alfa + P2.x * beta + P3.x * gamma
        centre_y = P1.y * alfa + P2.y * beta + P3.y * gamma

        radius = sqrt((centre_x - P1.x) ** 2 + (centre_y - P1.y) ** 2)

        return Circle(centre_x, centre_y, radius)


    @property
    def top(self):
        return self.pt.y + self.radius

    @property
    def left(self):
        return self.pt.x - self.radius

    @property
    def right(self):
        return self.pt.x + self.radius

    @property
    def bottom(self):
        return self.pt.y - self.radius

    @property
    def width(self):
        return 2 * self.radius

    @property
    def height(self):
        return 2 * self.radius

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)