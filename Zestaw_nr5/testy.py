import fracs
import unittest


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(fracs.add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(fracs.add_frac([-1, 2], [1, 5]), [-3, 10])

    def test_sub_frac(self):
        self.assertEqual(fracs.sub_frac([3, 6], [1, 3]), [1, 6])
        self.assertEqual(fracs.sub_frac([10, 6], [5, 8]), [25, 24])

    def test_mul_frac(self):
        self.assertEqual(fracs.mul_frac([5, 2], [3, 4]), [15, 8])
        self.assertEqual(fracs.mul_frac([-2, 2], [3, 4]), [-3, 4])

    def test_div_frac(self):
        self.assertEqual(fracs.div_frac([0, 2], [7, 3]), [0, 1])
        self.assertEqual(fracs.div_frac([7, 2], [-4, 3]), [21, -8])

    def test_is_positive(self):
        self.assertTrue(fracs.is_positive([2, 5]))
        self.assertFalse(fracs.is_positive([-5, 3]))

    def test_is_zero(self):
        self.assertTrue(fracs.is_zero([0, 10]))
        self.assertFalse(fracs.is_zero([-5, 3]))

    def test_cmp_frac(self):
        self.assertEqual(fracs.cmp_frac([9, 2], [-4, 3]), 1)
        self.assertEqual(fracs.cmp_frac([2, 3], [9, 4]), -1)
        self.assertEqual(fracs.cmp_frac([2, 3], [8, 12]), 0)

    def test_frac2float(self):
        self.assertEqual(fracs.frac2float([0, 3]), 0)
        self.assertEqual(fracs.frac2float([1, 2]), 0.5)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()