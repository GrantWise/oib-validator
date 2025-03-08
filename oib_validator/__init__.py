#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OIB Validator - Croatian Personal Identification Number validation.

This module provides functionality to validate Croatian Personal Identification Numbers (OIB).
"""

from .validator import OibValidator, validate_oib, main

__version__ = "0.1.0"
__all__ = ["OibValidator", "validate_oib", "main"] 