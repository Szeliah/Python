import pytest
from points import Point
from read_file import read_file
from convex_hull import convex_hull
from rotating_calipers import rotating_calipers


def test_1():
    file_1 = 'Data/points_1.txt'
    points = read_file(file_1)
    points_convex_hull = convex_hull(points)
    result = rotating_calipers(points_convex_hull)

    distance = result[0]
    first_point = result[1]
    second_point = result[2]

    assert pytest.approx(distance, rel=1e-3) == 10.049
    assert first_point == Point(-1, 3)
    assert second_point == Point(9, 2)


def test_2():
    file_1 = 'Data/points_2.txt'
    points = read_file(file_1)
    points_convex_hull = convex_hull(points)
    result = rotating_calipers(points_convex_hull)

    distance = result[0]
    first_point = result[1]
    second_point = result[2]

    assert pytest.approx(distance, rel=1e-3) == 15.132
    assert first_point == Point(-4, 2)
    assert second_point == Point(11, 0)


def test_3():
    file_1 = 'Data/points_3.txt'
    points = read_file(file_1)
    points_convex_hull = convex_hull(points)
    result = rotating_calipers(points_convex_hull)

    distance = result[0]
    first_point = result[1]
    second_point = result[2]

    assert pytest.approx(distance, rel=1e-3) == 7.071
    assert first_point == Point(6, 3)
    assert second_point == Point(1, -2)


def test_4():
    file_1 = 'Data/points_4.txt'
    points = read_file(file_1)
    points_convex_hull = convex_hull(points)
    result = rotating_calipers(points_convex_hull)

    distance = result[0]
    first_point = result[1]
    second_point = result[2]

    assert pytest.approx(distance, rel=1e-3) == 11
    assert first_point == Point(-2, 3)
    assert second_point == Point(9, 3)



def test_5():
    file_1 = 'Data/points_5.txt'
    points = read_file(file_1)
    points_convex_hull = convex_hull(points)
    result = rotating_calipers(points_convex_hull)

    distance = result[0]
    first_point = result[1]
    second_point = result[2]

    assert pytest.approx(distance, rel=1e-3) == 8.485
    assert first_point == Point(-4, 2)
    assert second_point == Point(2, -4)


if __name__ == '__main__':
     pytest.main()

