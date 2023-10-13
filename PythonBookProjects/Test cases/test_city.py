import unittest
from city_finctions import city


class CityTests(unittest.TestCase):
    def test_city(self):
        city_name = city('Prayagraj', 'India')
        self.assertEqual(city_name, "Prayagraj, India", "Error Message test not passed")


# if __name__ == '__main__':
#     unittest.main()
