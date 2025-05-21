#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for the OIB Validator.

This module contains unit tests for the OIB validation functionality.
"""
import unittest
from unittest.mock import patch, call
import io
import sys
from oib_validator import OibValidator, validate_oib
from oib_validator.validator import main


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

    def test_specific_algorithm_paths(self):
        """Test specific paths in the OIB validation algorithm."""
        # Test case for control_value becoming 0 during the loop.
        # OIB "00000000000" will have control_value = 10 initially.
        # 1st digit 0: (10 + 0) % 10 = 0. control_value becomes 10. (10 * 2) % 11 = 20 % 11 = 9.
        # 2nd digit 0: (9 + 0) % 10 = 9. (9 * 2) % 11 = 18 % 11 = 7.
        # 3rd digit 0: (7 + 0) % 10 = 7. (7 * 2) % 11 = 14 % 11 = 3.
        # 4th digit 0: (3 + 0) % 10 = 3. (3 * 2) % 11 = 6 % 11 = 6.
        # 5th digit 0: (6 + 0) % 10 = 6. (6 * 2) % 11 = 12 % 11 = 1.
        # 6th digit 0: (1 + 0) % 10 = 1. (1 * 2) % 11 = 2 % 11 = 2.
        # 7th digit 0: (2 + 0) % 10 = 2. (2 * 2) % 11 = 4 % 11 = 4.
        # 8th digit 0: (4 + 0) % 10 = 4. (4 * 2) % 11 = 8 % 11 = 8.
        # 9th digit 0: (8 + 0) % 10 = 8. (8 * 2) % 11 = 16 % 11 = 5.
        # 10th digit 0: (5 + 0) % 10 = 5. (5 * 2) % 11 = 10 % 11 = 10.
        # Final control_value = 10.
        # check_digit = 11 - 10 = 1.
        # So, "00000000000" should have check digit 1, making "00000000000" invalid.
        self.assertFalse(OibValidator.check("00000000000"))

        # Test case for an OIB where 11 - control_value == 10, leading to check_digit = 0.
        # "69435151530" is a known valid OIB with check digit 0.
        # Let's trace to confirm it hits the path:
        # Initial: cv = 10
        # 6: cv = ( (10+6)%10 * 2 )%11 = (6*2)%11 = 12%11 = 1
        # 9: cv = ( (1+9)%10 * 2 )%11 = (0*2)%11 -> cv becomes 10 -> (10*2)%11 = 9
        # 4: cv = ( (9+4)%10 * 2 )%11 = (3*2)%11 = 6
        # 3: cv = ( (6+3)%10 * 2 )%11 = (9*2)%11 = 7
        # 5: cv = ( (7+5)%10 * 2 )%11 = (2*2)%11 = 4
        # 1: cv = ( (4+1)%10 * 2 )%11 = (5*2)%11 = 10
        # 5: cv = ( (10+5)%10 * 2 )%11 = (5*2)%11 = 10
        # 1: cv = ( (10+1)%10 * 2 )%11 = (1*2)%11 = 2
        # 5: cv = ( (2+5)%10 * 2 )%11 = (7*2)%11 = 3
        # 3: cv = ( (3+3)%10 * 2 )%11 = (6*2)%11 = 1
        # Final control_value = 1. Check digit is 11 - 1 = 10. Since it's 10, check_digit becomes 0.
        # The 11th digit of "69435151530" is 0. So it's valid.
        self.assertTrue(OibValidator.check("69435151530")) # Already in test_algorithm_implementation

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('sys.argv', ['oib_validator/validator.py', '12345678903', '12345678901'])
    def test_main_with_args(self, mock_stdout):
        """Test main function with command-line arguments."""
        main()
        expected_output = "OIB 12345678903: Valid\nOIB 12345678901: Invalid\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['exit']) # Add mock for input
    @patch('sys.argv', ['oib_validator/validator.py'])
    def test_main_no_args(self, mock_input, mock_stdout): # Add mock_input
        """Test main function with no command-line arguments."""
        main()
        output = mock_stdout.getvalue()
        self.assertIn("OIB Validator - Test utility for Croatian Personal ID Numbers", output)
        self.assertIn("Usage:", output)
        self.assertIn("python -m oib_validator [OIB1] [OIB2] ...", output)
        self.assertIn("Running examples:", output)
        self.assertIn("Valid OIB test (12345678903): Valid", output)
        self.assertIn("Invalid OIB test (12345678901): Invalid", output)
        self.assertIn("Interactive mode (type 'exit' to quit):", output)


    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['12345678903', '12345678901', 'exit'])
    # No need to patch sys.argv here if main() is called with no args, it will enter interactive mode.
    # Patching sys.argv to ['oib_validator/validator.py'] is effectively the same as no args for this path.
    def test_main_interactive_mode(self, mock_input, mock_stdout):
        """Test main function in interactive mode."""
        # To isolate interactive mode, we ensure sys.argv implies no direct OIBs
        with patch('sys.argv', ['oib_validator/validator.py']):
            main()
        output = mock_stdout.getvalue()
        
        # Check for initial messages that are printed when no args are given
        self.assertIn("OIB Validator - Test utility for Croatian Personal ID Numbers", output)
        self.assertIn("Usage:", output)
        self.assertIn("Interactive mode (type 'exit' to quit):", output)
        
        # Check for interactive outputs (without the input prompt)
        # The input prompt "Enter an OIB to validate: " is not part of stdout
        self.assertIn("OIB 12345678903: Valid", output)
        self.assertIn("OIB 12345678901: Invalid", output)


if __name__ == "__main__":
    unittest.main() 