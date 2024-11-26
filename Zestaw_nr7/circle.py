#JEZYK PYTHON
#GRUPA CWICZENIOWA 02
#Zadania z zajec z dnia 20.11.2024
#Autor: Szymon Szeliga
from importlib.resources import open_text

from points import Point
from math import pi as PI
from math import sqrt

#W pliku circles.py zdefiniować klasę Circle wraz z potrzebnymi metodami.
#Okrąg jest określony przez podanie środka i promienia.
#Wykorzystać wyjątek ValueError do obsługi błędów. Napisać kod testujący moduł circles.


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

        if r1 > r2:          # zamiana zmiennych
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            r1, r2 = r2, r1

        distance = sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

        #Czy mniejszy okrag znajduje się cały w okregu wiekszym
        if r1 + distance <= r2:
            return Circle(x2, y2, r2)
        else:                                # obliczanie na podstawie promieni i dystansu
            r3 = (distance + r1 + r2) / 2
            factor = 0.5 + (r2 - r1) / (2 * distance)
            x3 = (1 - factor) * x1 + factor * x2
            y3 = (1 - factor) * y1 + factor * y2
            return Circle(x3, y3, r3)

