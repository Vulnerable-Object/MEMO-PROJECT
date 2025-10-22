#!/usr/bin/env python3
"""
Utility Functions for Crowdfunding Platform

This module contains helper functions for data validation and formatting.
These utilities ensure data integrity and provide consistent validation
across the entire application.

Functions:
- validate_email: Checks email format validity
- validate_egyptian_phone: Validates Egyptian mobile phone numbers
- format_currency: Formats numbers as Egyptian Pounds (EGP)
- is_valid_date: Validates date format and logical constraints

Author: Your Team
Version: 1.0
"""

import re
from datetime import datetime


def validate_email(email: str) -> bool:
    """
    Check if the email format is valid using regex pattern matching.
    
    Args:
        email (str): The email address to validate
        
    Returns:
        bool: True if email format is valid, False otherwise
        
    This function checks for:
    - Valid characters in username and domain
    - Presence of @ symbol
    - Valid domain structure with at least 2-character TLD
    
    Examples:
        >>> validate_email("user@example.com")
        True
        >>> validate_email("invalid.email")
        False
    """
    if not email or not isinstance(email, str):
        return False
        
    # Comprehensive email regex pattern
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email.strip()) is not None


def validate_egyptian_phone(phone: str) -> bool:
    """
    Check if the phone number is a valid Egyptian mobile number.
    
    Args:
        phone (str): The phone number to validate
        
    Returns:
        bool: True if valid Egyptian phone number, False otherwise
        
    Egyptian mobile numbers follow these patterns:
    - Start with 01 (country mobile prefix)
    - Second digit: 0, 1, 2, or 5 (network operators)
    - Followed by exactly 8 more digits
    - Total length: 11 digits
    
    Valid examples:
    - 01012345678 (Vodafone)
    - 01123456789 (Etisalat)
    - 01234567890 (Orange)
    - 01512345678 (WE)
    """
    if not phone or not isinstance(phone, str):
        return False
        
    # Remove any spaces or dashes that users might add
    clean_phone = phone.strip().replace(" ", "").replace("-", "")
    
    # Egyptian mobile pattern: 01[0125] followed by 8 digits
    egyptian_mobile_pattern = r'^01[0125][0-9]{8}$'
    return re.match(egyptian_mobile_pattern, clean_phone) is not None


def format_currency(amount: float, currency: str = "EGP") -> str:
    """
    Format a number as currency with proper thousands separators.
    
    Args:
        amount (float): The amount to format
        currency (str): Currency symbol (default: "EGP")
        
    Returns:
        str: Formatted currency string
        
    Examples:
        >>> format_currency(1500.50)
        "1,500.50 EGP"
        >>> format_currency(1000000)
        "1,000,000.00 EGP"
    """
    try:
        return f"{amount:,.2f} {currency}"
    except (ValueError, TypeError):
        return f"0.00 {currency}"


def is_valid_date_format(date_string: str) -> bool:
    """
    Check if a date string follows the YYYY-MM-DD format.
    
    Args:
        date_string (str): Date string to validate
        
    Returns:
        bool: True if valid format and date, False otherwise
    """
    try:
        datetime.strptime(date_string.strip(), "%Y-%m-%d")
        return True
    except (ValueError, AttributeError):
        return False


def dates_are_logical(start_date: str, end_date: str) -> bool:
    """
    Check if start date is before end date and both are valid.
    
    Args:
        start_date (str): Start date in YYYY-MM-DD format
        end_date (str): End date in YYYY-MM-DD format
        
    Returns:
        bool: True if dates are logical, False otherwise
    """
    try:
        start = datetime.strptime(start_date.strip(), "%Y-%m-%d")
        end = datetime.strptime(end_date.strip(), "%Y-%m-%d")
        return start < end
    except (ValueError, AttributeError):
        return False


def clean_text_input(text: str) -> str:
    """
    Clean and sanitize text input from users.
    
    Args:
        text (str): Raw text input
        
    Returns:
        str: Cleaned text with extra whitespace removed
    """
    if not text or not isinstance(text, str):
        return ""
    
    # Remove extra whitespace and strip
    return " ".join(text.strip().split())


def is_positive_number(value: str) -> bool:
    """
    Check if a string represents a positive number.
    
    Args:
        value (str): String to check
        
    Returns:
        bool: True if positive number, False otherwise
    """
    try:
        num = float(value.strip())
        return num > 0
    except (ValueError, AttributeError):
        return False
