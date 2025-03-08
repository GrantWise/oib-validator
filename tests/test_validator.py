#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for the OIB Validator.

This module contains unit tests for the OIB validation functionality.
"""
import unittest
from oib_validator import OibValidator, validate_oib


class TestOibValidator(unittest.TestCase):
    """Test case for the OIB Validator."""
    
    def test_valid_oib_string(self):
        """Test that a valid OIB string is correctly identified."""
        # This is a valid OIB for testing (verified with algorithm)
        valid_oib = "12345678903"
        self.assertTrue(OibValidator.validate(valid_oib))
        self.assertTrue(validate_oib(valid_oib))
    
    def test_valid_oib_int(self):
        """Test that a valid OIB integer is correctly identified."""
        # Same OIB as above but as an integer
        valid_oib = 12345678903
        self.assertTrue(OibValidator.validate(valid_oib))
        self.assertTrue(validate_oib(valid_oib))
    
    def test_invalid_oib(self):
        """Test that an invalid OIB is correctly rejected."""
        # This is an invalid OIB (wrong check digit)
        invalid_oib = "12345678901"
        self.assertFalse(OibValidator.validate(invalid_oib))
        self.assertFalse(validate_oib(invalid_oib))
    
    def test_wrong_length(self):
        """Test that an OIB with incorrect length is rejected."""
        # Too short
        self.assertFalse(OibValidator.validate("1234567890"))
        # Too long
        self.assertFalse(OibValidator.validate("123456789012"))
    
    def test_non_numeric(self):
        """Test that a non-numeric OIB is rejected."""
        self.assertFalse(OibValidator.validate("1234567890A"))
    
    def test_list_of_oibs(self):
        """Test validating a list of OIBs."""
        oibs = ["12345678903", "12345678901"]
        result = validate_oib(oibs)
        self.assertEqual(result, {"12345678903": True, "12345678901": False})
    
    def test_algorithm_implementation(self):
        """Test that our algorithm implementation correctly validates OIBs."""
        # Test with manually verified valid OIBs
        # Example 1: Generated from our algorithm
        self.assertTrue(validate_oib("12345678903"))
        
        # Example 2: Real Croatian OIB with check digit 0
        self.assertTrue(validate_oib("69435151530"))
        
        # Test with invalid OIB
        self.assertFalse(validate_oib("12345678901"))


if __name__ == "__main__":
    unittest.main() 