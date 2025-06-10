def exponetial_parser(exp: str) -> float:
    """
    Parses an exponential expression of the form 'a^b' and returns the result.
    
    :param exp: A string representing the exponential expression.
    :return: The result of the exponential calculation.
    """
    try:
        base, exponent = exp.split('^')
        base = float(base.strip())
        exponent = float(exponent.strip())
        return base ** exponent
    except ValueError:
        raise ValueError("Invalid format. Use 'a^b' where a and b are numbers.")
    
def squareroot_parser(exp: str) -> float:
    """
    Parses a square root expression of the form 'sqrt(a)' and returns the result.
    
    :param exp: A string representing the square root expression.
    :return: The result of the square root calculation.
    """
    try:
        if exp.startswith('sqrt(') and exp.endswith(')'):
            number = float(exp[5:-1].strip())
            if number < 0:
                raise ValueError("Cannot compute square root of a negative number.")
            return number ** 0.5
        else:
            raise ValueError("Invalid format. Use 'sqrt(a)' where a is a number.")
    except ValueError:
        raise ValueError("Invalid input for square root calculation.")
def logarithm_parser(exp: str) -> float:
    """
    Parses a logarithm expression of the form 'log(a, b)' and returns the result.
    
    :param exp: A string representing the logarithm expression.
    :return: The result of the logarithm calculation.
    """
    try:
        if exp.startswith('log(') and exp.endswith(')'):
            args = exp[4:-1].split(',')
            if len(args) != 2:
                raise ValueError("Invalid format. Use 'log(a, b)' where a is the number and b is the base.")
            number = float(args[0].strip())
            base = float(args[1].strip())
            if number <= 0 or base <= 0 or base == 1:
                raise ValueError("Invalid input for logarithm calculation.")
            import math
            return math.log(number, base)
        else:
            raise ValueError("Invalid format. Use 'log(a, b)' where a is the number and b is the base.")
    except ValueError:
        raise ValueError("Invalid input for logarithm calculation.")

def parse_expression(exp: str) -> float:
    """
    Parses a mathematical expression and returns the result.
    
    :param exp: A string representing the mathematical expression.
    :return: The result of the calculation.
    """
    exp = exp.strip()
    
    if '^' in exp:
        return exponetial_parser(exp)
    elif exp.startswith('sqrt(') and exp.endswith(')'):
        return squareroot_parser(exp)
    elif exp.startswith('log(') and exp.endswith(')'):
        return logarithm_parser(exp)
    else:
        raise ValueError("Unsupported expression format.")

