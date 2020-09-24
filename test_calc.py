import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(100, 1), 101)
        self.assertEqual(calc.add(-88, 88), 0)
        self.assertEqual(calc.add(2, 2), 4)

    def test_subtract(self):
        self.assertEqual(calc.subtract(4, 2), 2)
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(12, 6), 6)

    def test_divide(self):
        self.assertEqual(calc.divide(4, 2), 2)
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(12, 6), 2)
        # self.assertRaises(ValueError, calc.divide, 10, 0)
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(4, 2), 8)
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(12, 6), 72)



if __name__ == '__main__':
    unittest.main()