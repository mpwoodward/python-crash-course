import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Joe', 'Blow', 100000)
    
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 105000)
    
    def test_give_custom_raise(self):
        self.employee.give_raise(17000)
        self.assertEqual(self.employee.salary, 117000)


unittest.main()
