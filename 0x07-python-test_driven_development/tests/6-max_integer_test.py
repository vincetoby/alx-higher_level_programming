#!/usr/bin/python3
"""
    unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ the class for unittests """
    def max_integer_tester(self):
        """ check possible test cases """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-4]), -4)
        self.assertEqual(max_integer([-9, -2, -3]), -2)
        self.assertEqual(max_integer([15, 10, 150]), 150)
        self.assertEqual(max_integer([15, 10, 5, -5, -10, 15]), 15)
        self.assertEqual(max_integer([11, 11, 11]), 11)

    def type_error_tester(self):
        """ type errors """
        self.assertRaises(TypeError, max_integer, ["h", 1])
        self.assertRaises(TypeError, max_integer, [2, [2, 1]])
