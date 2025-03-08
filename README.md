# OIB Validator

A Python utility for validating Croatian Personal Identification Numbers (OIB).

## Description

The OIB (Osobni identifikacijski broj) is a unique 11-digit personal identification number assigned to each Croatian citizen and resident. This utility validates OIB numbers using the ISO 7064, MOD 11-10 algorithm.

## Features

- Validate single OIB numbers
- Validate multiple OIB numbers at once
- Support for both string and integer input formats
- Command-line interface for easy validation
- Interactive mode for testing multiple OIBs

## Installation

### Option 1: Clone the repository

```bash
git clone https://github.com/GrantWise/oib-validator.git
cd oib-validator
```

### Option 2: Install via pip (coming soon)

```bash
pip install oib-validator
```

## Usage

### As a module in your code

```python
from oib_validator import validate_oib

# Validate a single OIB
result = validate_oib("12345678903")  # Valid OIB
print(f"Valid: {result}")  # Valid: True

# Validate multiple OIBs at once
results = validate_oib(["12345678903", "12345678901"])
print(results)  # {'12345678903': True, '12345678901': False}
```

### Command line usage

```bash
# Validate one or more OIBs
python -m oib_validator 12345678903 12345678901

# Run in interactive mode (no arguments)
python -m oib_validator
```

## Algorithm

The OIB validation uses the ISO 7064, MOD 11-10 algorithm:

1. Start with control value 10
2. For each of the first 10 digits:
   - Add the digit to the control value
   - If control value is 0, set it to 10
   - Take the result modulo 10
   - Multiply by 2
   - Take the result modulo 11
3. Calculate check digit: 11 - final control value (if result is 10, check digit is 0)
4. The OIB is valid if the calculated check digit matches the 11th digit

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Acknowledgments

- Croatian Tax Administration for the OIB specification
- ISO 7064 standard for the check digit algorithm 