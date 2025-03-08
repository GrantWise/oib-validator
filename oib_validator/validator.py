#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OIB Validator - Croatian Personal Identification Number validation.

This module provides functionality to validate Croatian Personal Identification Numbers (OIB).
OIB (Osobni identifikacijski broj) is a unique 11-digit personal identification number 
assigned to each Croatian citizen and resident. The number consists of 10 randomly 
generated digits plus a final check digit that is calculated using the ISO 7064, MOD 11-10
algorithm.
"""
from typing import Union, Dict, List, Optional, TypeVar, Callable, Any

# Create a type variable for the OIB type - can be str or int
OibType = TypeVar('OibType', str, int)


class OibValidator:
    """
    Validator for Croatian Personal Identification Numbers (OIB).
    
    The OIB consists of 11 digits total:
    - 10 digits that form the base number
    - 1 check digit that is calculated using the ISO 7064, MOD 11-10 algorithm
    
    This class provides methods to validate both individual OIBs and collections of OIBs.
    
    Attributes:
        LENGTH (int): The required length of a valid OIB (11 digits).
    """
    
    LENGTH: int = 11
    
    @classmethod
    def validate(cls, data: Union[OibType, List[OibType]]) -> Union[bool, Dict[str, bool]]:
        """
        Validates a single OIB or a list of OIBs.
        
        This method serves as a facade that handles different input types:
        - If given a single OIB (as string or int), it will validate just that OIB
        - If given a list of OIBs, it will validate each one and return results as a dictionary
        
        Args:
            data: A single OIB as string or integer, or a list of OIBs
                 to validate.
        
        Returns:
            Union[bool, Dict[str, bool]]: If a single OIB is provided, returns a boolean 
                indicating if it's valid. If a list is provided, returns a dictionary 
                mapping each OIB to its validation result.
        """
        # Handle list input - validate each OIB in the list
        if isinstance(data, list):
            result: Dict[str, bool] = {}
            for oib in data:
                # Convert each OIB to string for use as dictionary key
                result[str(oib)] = cls.check(oib)
            return result
        
        # Handle single OIB input
        return cls.check(data)
    
    @classmethod
    def check(cls, data: OibType) -> bool:
        """
        Validates a single OIB using the ISO 7064, MOD 11-10 algorithm.
        
        The validation process:
        1. Verify the input is a numeric string of exactly 11 digits
        2. Calculate a control digit based on the first 10 digits
        3. Compare the calculated control digit with the 11th digit of the OIB
        
        Args:
            data: The OIB to validate as string or integer.
            
        Returns:
            bool: True if the OIB is valid, False otherwise.
        """
        # Convert to string if it's an integer to allow string operations
        data_str: str = str(data)
        
        # Perform basic validation: must be all digits and exactly 11 characters
        if data_str.isdigit() and len(data_str) == cls.LENGTH:
            # ====== ISO 7064, MOD 11-10 Checksum Algorithm ======
            
            # Start with control value 10
            control_value: int = 10
            
            # Process the first 10 digits
            for i in range(10):
                # Get the current digit
                current_digit: int = int(data_str[i])
                
                # Step 1: Add the current digit to the control value
                # Step 2: Take the result modulo 10 (keep only the last digit)
                control_value = (control_value + current_digit) % 10
                
                # Step 3: If control value is 0, set it to 10 (special case)
                if control_value == 0:
                    control_value = 10
                    
                # Step 4: Multiply by 2
                # Step 5: Take the result modulo 11
                control_value = (control_value * 2) % 11
            
            # Calculate the check digit:
            # - Subtract the final control value from 11
            # - If the result is 10, the check digit is 0 (special case in the algorithm)
            # - Otherwise, the check digit is the result itself
            check_digit: int = 0 if 11 - control_value == 10 else 11 - control_value
            
            # The OIB is valid if the calculated check digit matches the 11th digit
            return check_digit == int(data_str[10])
        
        # If we got here, validation failed (not all digits or wrong length)
        return False


def validate_oib(data: Union[OibType, List[OibType]]) -> Union[bool, Dict[str, bool]]:
    """
    Convenience function to validate OIB(s) without directly using the OibValidator class.
    
    This function simply delegates to the OibValidator class, providing a simpler interface
    for users who don't need to interact with the class directly.
    
    Args:
        data: A single OIB as string or integer, or a list of OIBs
             to validate.
    
    Returns:
        Union[bool, Dict[str, bool]]: If a single OIB is provided, returns a boolean 
            indicating if it's valid. If a list is provided, returns a dictionary 
            mapping each OIB to its validation result.
        
    Examples:
        >>> validate_oib("12345678901")  # Validate a single OIB (invalid)
        False
        >>> validate_oib("12345678903")  # Validate a single OIB (valid)
        True
        >>> validate_oib(["12345678903", "12345678901"])  # Validate multiple OIBs
        {'12345678903': True, '12345678901': False}
    """
    return OibValidator.validate(data)


def main() -> None:
    """
    Main entry point for command-line usage.
    
    Provides a simple command-line interface for validating OIB numbers either
    through command-line arguments or an interactive prompt.
    
    Returns:
        None
    """
    import sys
    
    # If command line arguments are provided, validate those OIBs
    if len(sys.argv) > 1:
        # Validate each OIB provided as command line argument
        for oib in sys.argv[1:]:
            result = validate_oib(oib)
            print(f"OIB {oib}: {'Valid' if result else 'Invalid'}")
    else:
        # No arguments provided, show usage and example
        print("OIB Validator - Test utility for Croatian Personal ID Numbers")
        print("\nUsage:")
        print("  python -m oib_validator [OIB1] [OIB2] ...")
        print("\nExample:")
        print("  python -m oib_validator 12345678903 12345678901")
        print("\nRunning examples:")
        
        valid_oib = "12345678903"  # This is a valid OIB for demonstration
        invalid_oib = "12345678901"  # This is invalid (wrong check digit)
        
        print(f"Valid OIB test ({valid_oib}): {'Valid' if validate_oib(valid_oib) else 'Invalid'}")
        print(f"Invalid OIB test ({invalid_oib}): {'Valid' if validate_oib(invalid_oib) else 'Invalid'}")
        
        # Interactive mode
        print("\nInteractive mode (type 'exit' to quit):")
        while True:
            user_input = input("Enter an OIB to validate: ")
            if user_input.lower() in ('exit', 'quit', 'q'):
                break
            if user_input:
                is_valid = validate_oib(user_input)
                print(f"OIB {user_input}: {'Valid' if is_valid else 'Invalid'}")


if __name__ == "__main__":
    main() 