import re
def validate_email_password(email, password):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if not email or not password:
        return False, "Email and password are required"
    
    if len(password) < 6:
        return False, "Password should be at least 6 characters long"
    
    if not re.fullmatch(regex, email):
        return False, "Invalid email format"
    
    return True, None
