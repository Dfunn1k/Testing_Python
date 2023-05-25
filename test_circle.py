from math import pi
from circle import area_circle
import unittest

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # Test areas when radius >= 0
        self.assertAlmostEqual(area_circle(1), pi)
        self.assertAlmostEqual(area_circle(0), 0)
        self.assertAlmostEqual(area_circle(2.3), pi*(2.3**2))

    def test_values(self):
        # Make sure value errors are raised when necessary
        self.assertRaises(ValueError, area_circle, -2)

    def test_types(self):
        # Make sure type errors are raised when neccesary
        self.assertRaises(TypeError, area_circle, 2+5j)
        self.assertRaises(TypeError, area_circle, True)
        self.assertRaises(TypeError, area_circle, "2")