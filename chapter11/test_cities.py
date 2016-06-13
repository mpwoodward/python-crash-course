import unittest

from city_functions import city_country


class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        s = city_country('vienna', 'austria')
        self.assertEqual(s, 'Vienna, Austria')


unittest.main()
