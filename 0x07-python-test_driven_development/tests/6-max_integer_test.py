#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_positive(self):
        """Test case for a list of positive integers
        """
        self.assertEqual(max_integer([2, 3, 5, 9, 6]), 9)

    def test_max_negative(self):
        """Test case for a list of negative integers
        """
        self.assertEqual(max_integer([-1, -3, -10, -25, -4]), -1)

    def test_max_empty_list(self):
        """Test case for an empty list
        """
        self.assertIsNone(max_integer([]))

    def test_max_mixed(self):
        """Test case for a list of mixed positive and negative integers
        """
        self.assertEqual(max_integer([-1, 3, 0, -5, 4]), 4)

    def test_max_single_element(self):
        """Test case for a list with a single element
        """
        self.assertEqual(max_integer([5]), 5)

    def test_max_duplicate_values(self):
        """Test case for a list with duplicate values
        """
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_max_mixed_types(self):
        """Test case for raise TypeError
        """
        with self.assertRaises(TypeError):
            max_integer([0, 2, '8', 5])

    def test_max_large_values(self):
        """Test case for a list with large values
        """
        self.assertEqual(max_integer([5000000, 500000, 50000, 9000]), 5000000)
