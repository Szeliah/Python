# Kod testujący moduł.

import unittest
from circle import Circle
from math import sqrt

class TestCircle(unittest.TestCase):

    def setUp(self): pass

    def test_return_repr_string(self):
        new_circle_1 = Circle(1, 2, 3)
        new_circle_2 = Circle(4, 5, 12)
        self.assertEqual(new_circle_1.__str__(), "Circle(1, 2, 3)")
        self.assertEqual(new_circle_2.__str__(), "Circle(4, 5, 12)")


    def test_eq_circle(self):
        new_circle_1 = Circle(1, 2, 3)
        new_circle_2 = Circle(4, 5, 12)
        self.assertTrue(new_circle_1 == Circle(1, 2, 3))
        self.assertFalse(new_circle_2.__eq__(Circle(4, 4, 12)))


    def test_ne_circle(self):
        new_circle_1 = Circle(5, 5, 5)
        new_circle_2 = Circle(4, 5, 12)
        self.assertTrue(new_circle_1 != Circle(10, 10, 10))
        self.assertFalse(new_circle_2.__ne__(Circle(4, 5, 12)))


    def test_area_circle(self):
        new_circle_1 = Circle(5, 5, 5)
        new_circle_2 = Circle(4, 5, 3)
        self.assertAlmostEquals(new_circle_1.area(), 78.5398, 4)
        self.assertAlmostEquals(new_circle_2.area(),28.2743, 4)


    def test_move_circle(self):
        new_circle_1 = Circle(5, 5, 5)
        new_circle_2 = Circle(4, 5, 3)
        new_circle_1.move(2, 2)
        new_circle_2.move(3, 5)
        self.assertEqual(new_circle_1, Circle(7, 7, 5))
        self.assertEqual(new_circle_2, Circle(7, 10, 3))

    def test_cover_circle(self):
        new_circle_1 = Circle(2, 2, 2)
        new_circle_2 = Circle(6, 2, 2)
        self.assertEqual(new_circle_1.cover(new_circle_2), Circle(4, 2, 4))

        new_circle_3 = Circle(5, 6, 10)
        new_circle_4 = Circle(7, 6, 2)
        self.assertEqual(Circle.cover(new_circle_3, new_circle_4), Circle(5, 6, 10))

        new_circle_5 = Circle(5, 5, sqrt(2))
        new_circle_6 = Circle(2.5, 2.5, sqrt(0.5))
        self.assertEqual(new_circle_5.cover(new_circle_6), Circle(4, 4, sqrt(8)))


    def tearDown(self): pass



if __name__ == '__main__':
        unittest.main()

