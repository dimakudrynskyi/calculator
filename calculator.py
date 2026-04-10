def add(a, b):
    """
    Add two numbers together.
    
    Args:
        a: First number (int or float)
        b: Second number (int or float)
    
    Returns:
        The sum of a and b
    
    Raises:
        TypeError: If operands are not numbers
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Operands must be numbers")
    
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("Operands must be numbers")
    
    return a + b


def subtract(a, b):
    """
    Subtract b from a.
    
    Args:
        a: First number (int or float)
        b: Second number (int or float)
    
    Returns:
        The difference of a and b
    
    Raises:
        TypeError: If operands are not numbers
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Operands must be numbers")
    
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("Operands must be numbers")
    
    return a - b


def multiply(a, b):
    """
    Multiply two numbers together.
    
    Args:
        a: First number (int or float)
        b: Second number (int or float)
    
    Returns:
        The product of a and b
    
    Raises:
        TypeError: If operands are not numbers
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Operands must be numbers")
    
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("Operands must be numbers")
    
    return a * b


def divide(a, b):
    """
    Divide a by b.
    
    Args:
        a: Dividend (int or float)
        b: Divisor (int or float)
    
    Returns:
        The quotient of a divided by b (float)
    
    Raises:
        TypeError: If operands are not numbers
        ZeroDivisionError: If b is zero
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Operands must be numbers")
    
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("Operands must be numbers")
    
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    
    return a / b


def validate_input(value):
    """
    Validate and convert input to a number.
    
    Args:
        value: Input value to validate
    
    Returns:
        Converted number (int or float)
    
    Raises:
        ValueError: If value cannot be converted to a number
    """
    try:
        if '.' in str(value):
            return float(value)
        else:
            return int(value)
    except (ValueError, AttributeError):
        raise ValueError(f"Invalid input: '{value}' is not a valid number")
