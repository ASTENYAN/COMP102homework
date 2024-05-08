import unittest
from AgeCheck import young_driver_age, older_driver_age, elderly_driver_age, \
    young_driver_premium_multiplier, older_driver_premium_multiplier, elderly_driver_premium_multiplier, \
    young_driver_experience_multiplier, no_multiplier, young_driver_experience, older_driver_experience

from AgeCheck import agecheck


class TestAgeCheck(unittest.TestCase):
    def test_1(self):
        # Test a young driver with low experience
        x= 20
        y= 1
        expected= young_driver_premium_multiplier * young_driver_experience_multiplier
        self.assertEqual(agecheck(x, y), expected)
    def test_2(self):
        # Test a young driver
        x= 20
        y= 3
        expected= young_driver_premium_multiplier
        self.assertEqual(agecheck(x, y), expected)
    def test_3(self):
        # Test a middle-aged driver with low experience
        x = 75
        y = 4
        expected= older_driver_premium_multiplier
        self.assertEqual(agecheck(x, y), expected)
    def test_4(self):
        # Test an elderly driver
        x= 85
        y= 6
        expected= elderly_driver_premium_multiplier
        self.assertEqual(agecheck(x, y), expected)
    def test_boundary(self):
        # Test for boundaries of age and experience
        x= 25
        y= 2
        expected= young_driver_premium_multiplier * young_driver_experience_multiplier
        self.assertEqual(agecheck(x, y), expected)

if __name__ == '_main_':
    tests = unittest.TestLoader().loadTestsFromTestCase(TestAgeCheck)
    testRunner = unittest.TextTestRunner(verbosity=2)
    result = testRunner.run(tests)
    if result.wasSuccessful():
        print("All tests passed!")
    else:
        print("Some tests failed.")