import unittest
from points import Point
from triangles import Triangle

class TestTriangle(unittest.TestCase):

    def setUp(self): pass

    def test_return_basic_string(self):
        new_triangle = Triangle(1, 1, 3, 1, 1, 3)
        self.assertEqual(new_triangle.__str__(), "[(1, 1), (3, 1), (1, 3)]")

    def test_return_repr_string(self):
        new_triangle = Triangle(1, 1, 3, 1, 1, 3)
        self.assertEqual(new_triangle.__repr__(), "Triangle(1, 1, 3, 1, 1, 3)")

    def test_eq_traingle(self):
        new_triangle = Triangle(1, 1, 3, 1, 1, 3)
        self.assertTrue(new_triangle == Triangle(1, 1, 3, 1, 1 ,3))
        self.assertFalse(new_triangle.__eq__(Triangle(3, 4, 1, 2, 6, 7)))

    def test_ne_triagnle(self):
        new_triangle = Triangle(1, 1, 3, 1, 1, 3)
        self.assertFalse(new_triangle != Triangle(1, 1, 3, 1, 1, 3))
        self.assertTrue(new_triangle.__ne__(Triangle(3, 4, 1, 2, 6, 7)))

    def test_centre_triangle(self):
        new_triangle_1 = Triangle(3, 6, 3, 3, 3, 9)
        new_triangle_2 = Triangle(3, 5, 3, 1, 6, 3)
        self.assertEqual(new_triangle_1.center(), Point(3, 6))
        self.assertEqual(new_triangle_2.center(), Point(4, 3))

    def test_area_triangle(self):
        new_triangle_1 = Triangle(1, 1, 3, 1, 1, 3)
        new_triangle_2 = Triangle(1, 1, 7, 1, 1, 8)
        new_triangle_3 = Triangle(0, 0, 2, 4, 5, 0)
        self.assertEqual(new_triangle_1.area(), 2 )
        self.assertEqual(new_triangle_2.area(), 21)
        self.assertEqual(new_triangle_3.area(), 10)


    def test_move_triangle(self):
        new_triangle_1 = Triangle(1, 1, 3, 1, 1, 3)
        new_triangle_1.move(4, 5)
        self.assertTrue(new_triangle_1 == Triangle(5, 6, 7, 6, 5, 8 ))


    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()