#JEZYK PYTHON
#GRUPA CWICZENIOWA 02
#Zadania z zajec z dnia 27.11.2024
#Autor: Szymon Szeliga


# Kod testujący moduł.
from circle import Circle
from points import Point
import pytest
from math import pi as PI

def test_eq():
    circle_1 = Circle(4,5,6)
    circle_2 = Circle(6,7, 2)
    assert circle_1 == Circle(4,5,6)
    assert circle_1 != circle_2

def test_area():
    circle_1 = Circle(4, 5, 6)
    circle_2 = Circle(6, 7, 2)
    assert pytest.approx(circle_1.area(), rel=1e-4) == 113.0973
    assert pytest.approx(circle_2.area(), rel=1e-5) == 4 * PI

def test_properties():
    circle_1 = Circle(6,7,5)
    assert circle_1.top == 12
    assert circle_1.bottom == 2
    assert circle_1.left == 1
    assert  circle_1.right == 11

    assert circle_1.width == 10
    assert circle_1.topright == Point(11, 12)
    assert circle_1.topleft == Point(1, 12)
    assert circle_1.bottomright == Point(11, 2)
    assert circle_1.bottomleft == Point(1, 2)

def test_from_points():
    points_1 = (Point(0,3), Point(3,0), Point(0,-3))
    circle = Circle.from_points(points_1)
    assert circle.pt.x == 0
    assert circle.pt.y == 0
    assert circle.radius == 3

    points_2 = (Point(1.815287, 3.1525), Point(-0.5511, 2.14251), Point(5.687351, -3.51985532))
    circle_2 = Circle.from_points(points_2)
    assert pytest.approx(circle_2.pt.x, rel=1e-8) ==  2.2197930397213046
    assert pytest.approx(circle_2.pt.y, rel=1e-8) == -1.0724442576188693
    assert pytest.approx(circle_2.radius, rel=1e-8) == 4.244264260876986


if __name__ == '__main__':
    pytest.main()

