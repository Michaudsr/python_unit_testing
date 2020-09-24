import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Test for Employee class"""

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    def setUp(self):
        print('setUp')
        self.levin = Employee('Levin', 'Batallones', 200000)
        self.martin = Employee('Martin', 'Briceno', 199999)
        self.steven = Employee('Steven', 'Michaud', 100000)
        self.adam = Employee('Adam', 'Honore', 200000)

    def tearDown(self):
        print('tearDown\n')


    def test_email(self):
        self.assertEqual(self.steven.email, 'steven.michaud@sei713.com')
        self.assertEqual(self.martin.email, 'martin.briceno@sei713.com')
        self.assertEqual(self.levin.email, 'levin.batallones@sei713.com')
        self.assertEqual(self.adam.email, 'adam.honore@sei713.com')
        

    def test_fullname(self):
        self.assertEqual(self.steven.fullname, 'Steven Michaud')
        self.assertEqual(self.adam.fullname, 'Adam Honore')

    def test_raise_amount(self):
        self.steven.apply_raise()
        self.adam.apply_raise()
        self.assertEqual(self.adam.pay, 230000)
        self.assertEqual(self.steven.pay, 115000)


if __name__ == '__main__':
    unittest.main()