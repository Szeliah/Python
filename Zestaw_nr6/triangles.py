#JEZYK PYTHON
#GRUPA CWICZENIOWA 02
#Zadania z zajec z dnia 13.11.2024
#Autor: Szymon Szeliga

from select import select
from math import sqrt

# Zadanie 6.4
# OPIS ZADANIA
#W pliku triangles.py zdefiniować klasę Triangle wraz z potrzebnymi metodami.
#Trójkąt jest określony przez podanie trzech wierzchołków. Napisać kod testujący moduł triangles.


from points import Point

class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)


     # "[(x1, y1), (x2, y2), (x3, y3)]"
    def __str__(self):
        return f"[{self.pt1.__str__()}, {self.pt2.__str__()}, {self.pt3.__str__()}]"


    # "Triangle(x1, y1, x2, y2, x3, y3)"
    def __repr__(self):
        return f"Triangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}, {self.pt3.x}, {self.pt3.y})"


    # obsługa tr1 == tr2
    def __eq__(self, other):
        # Trójkąty powinny być równe, jeżeli mają ten sam zbiór wierzchołków,
        # niezależnie od kolejności pt1, pt2, pt3.
        vertex_of_self = {self.pt1, self.pt2, self.pt3}
        vertex_of_other = {other.pt1, other.pt2, other.pt3}
        return vertex_of_self.__eq__(vertex_of_other)


    # obsługa tr1 != tr2
    def __ne__(self, other):
        return not self == other


    # zwraca środek (masy) trójkąta
    def center(self):
        x_center = (self.pt1.x + self.pt2.x + self.pt3.x) / 3
        y_center = (self.pt1.y + self.pt2.y + self.pt3.y) / 3
        return Point(x_center, y_center)


    # pole powierzchni
    def area(self):
        vector_ab = self.pt1 - self.pt2
        vector_ac = self.pt1 - self.pt3
        area = abs(Point.cross(vector_ab, vector_ac)) / 2
        return area


    # przesunięcie o (x, y)
    def move(self, x, y):
        self.pt1.x = self.pt1.x + x
        self.pt2.x = self.pt2.x + x
        self.pt3.x = self.pt3.x + x
        self.pt1.y = self.pt1.y + y
        self.pt2.y = self.pt2.y + y
        self.pt3.y = self.pt3.y + y



