import unittest
from points import Point

class TestPoint(unittest.TestCase):

    def setUp(self): pass

    def test_return_basic_string(self):
        new_point_1 = Point(1,1)
        new_point_2 = Point(4, 12)
        self.assertEqual(new_point_1.__str__(), "(1, 1)")
        self.assertEqual(new_point_2.__str__(), "(4, 12)")

    def test_return_repr_string(self):
        new_point_1 = Point(2,2)
        new_point_2 = Point(4,5)
        self.assertEqual(new_point_1.__repr__(), "Point(2, 2)")
        self.assertEqual(new_point_2.__repr__(), "Point(4, 5)")

    def test_eq_points(self):
        new_point_1 = Point(4, 5)
        new_point_2 = Point(7 ,5)
        self.assertTrue(new_point_1 == Point(4, 5))
        self.assertFalse(new_point_2.__eq__(Point(7, 6)))

    def test_ne_points(self):
        new_point_1 = Point(6, 5)
        new_point_2 = Point(9, 5)
        self.assertTrue(new_point_1 != Point(4, 5))
        self.assertFalse(new_point_2.__ne__(Point(9, 5)))

    def test_add_points(self):
        new_point_1 = Point(3, 3)
        new_point_2 = Point(6 , 8)
        self.assertEqual(new_point_1 + Point(3,3), Point(6, 6))
        self.assertEqual(new_point_2.__add__(Point(1, 2)), Point(7, 10))

    def test_sub_points(self):
        new_point_1 = Point(10, 10)
        new_point_2 = Point(5, 6)
        self.assertEqual(new_point_1 - Point(5 , 7), Point(5, 3))
        self.assertEqual(new_point_2.__sub__(Point(2, 5)), Point(3, 1))

    def test_mul_points(self):
        new_point_1 = Point(3, 4)
        new_point_2 = Point(6, 7)
        self.assertEqual(new_point_1 * Point(3 , 4), 25)
        self.assertEqual(new_point_2.__mul__(Point(2, 3)), 33)

    def test_cross_points(self):
        new_point_1 = Point(3 ,3)
        new_point_2 = Point(4 ,5)
        self.assertEqual(Point.cross(new_point_1, Point(5, 5)), 0)
        self.assertEqual(Point.cross(new_point_2, Point(2, 10)), 30)

    def test_length_points(self):
        new_point_1 = Point(4, 3)
        new_point_2 = Point(0, 2)
        self.assertEqual(Point.length(new_point_1), 5)
        self.assertEqual(Point.length(new_point_2), 2)

    def test_hash_points(self):
        new_point_1 = Point(3, 4)
        new_point_2 = Point(6 , 8)
        self.assertTrue(new_point_1.__hash__() != Point(4, 3).__hash__())
        self.assertTrue(new_point_2.__hash__() == Point(6, 8).__hash__())


    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()