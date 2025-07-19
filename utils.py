import re

def validate_email(email: str) -> bool:
    """Check if the email format is valid."""
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$', email) is not None

def validate_egyptian_phone(phone: str) -> bool:
    """Check if the phone number is a valid Egyptian number."""
    return re.match(r'^01[0125][0-9]{8}$', phone) is not None
