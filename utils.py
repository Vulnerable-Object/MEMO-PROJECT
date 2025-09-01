import re
from typing import Optional
from datetime import datetime


def validate_email(email: str) -> bool:
    """
    Validate email format using regex pattern.
    
    Args:
        email (str): The email address to validate
        
    Returns:
        bool: True if email format is valid, False otherwise
    """
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email) is not None


def validate_egyptian_phone(phone: str) -> bool:
    """
    Validate Egyptian phone number format.
    Egyptian numbers start with 010, 011, 012, or 015 followed by 8 digits.
    
    Args:
        phone (str): The phone number to validate
        
    Returns:
        bool: True if phone number is valid Egyptian format, False otherwise
    """
    pattern = r'^01[0125][0-9]{8}$'
    return re.match(pattern, phone) is not None


def validate_date_format(date_string: str) -> Optional[datetime]:
    """
    Validate and parse date string in YYYY-MM-DD format.
    
    Args:
        date_string (str): Date string to validate
        
    Returns:
        Optional[datetime]: Parsed datetime object if valid, None otherwise
    """
    try:
        return datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        return None


def validate_date_range(start_date: str, end_date: str) -> bool:
    """
    Validate that start date is before end date.
    
    Args:
        start_date (str): Start date in YYYY-MM-DD format
        end_date (str): End date in YYYY-MM-DD format
        
    Returns:
        bool: True if date range is valid, False otherwise
    """
    start = validate_date_format(start_date)
    end = validate_date_format(end_date)
    
    if start is None or end is None:
        return False
    
    return start < end


def format_currency(amount: float) -> str:
    """
    Format currency amount with proper formatting.
    
    Args:
        amount (float): The amount to format
        
    Returns:
        str: Formatted currency string
    """
    return f"{amount:,.2f} EGP"


def get_user_input(prompt: str, input_type: type = str, validator=None):
    """
    Get validated user input with optional type conversion and validation.
    
    Args:
        prompt (str): The input prompt to display
        input_type (type): The expected type (str, int, float)
        validator (callable): Optional validation function
        
    Returns:
        The validated input value
    """
    while True:
        try:
            value = input(prompt)
            
            if input_type != str:
                value = input_type(value)
            
            if validator and not validator(value):
                print("Invalid input. Please try again.")
                continue
                
            return value
            
        except ValueError:
            print(f"Please enter a valid {input_type.__name__}.")
            continue
