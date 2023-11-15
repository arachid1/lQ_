import pkg_resources, subprocess, unittest, sys, importlib
from pathlib import Path
import os
import sys

sys.path.append("..")

from lQ_.main import linear_equation


class TestLinearEquation(unittest.TestCase):
    def setUp(self):
        self.x = 2

    def tearDown(self):
        del self.x

    def test_linear_equation_equal_successful(self):
        self.assertEqual(linear_equation(self.x), 7)

    def test_linear_equation_not_equal_successful(self):
        self.assertNotEqual(linear_equation(self.x), 4)

    def test_linear_equation_wrong_input_type_unsuccessful(self):
        with self.assertRaises(TypeError):
            linear_equation("fdlj")
