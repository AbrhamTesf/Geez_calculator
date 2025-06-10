def integration(interval, function):
    """
    A simple numerical integration using the trapezoidal rule.
    
    :param interval: A tuple (a, b) representing the interval of integration.
    :param function: A callable function to integrate.
    :return: The approximate value of the integral.
    """
    a, b = interval
    n = 1000  # Number of subintervals
    h = (b - a) / n  # Width of each subinterval
    total = 0.5 * (function(a) + function(b))  # Start with the endpoints

    for i in range(1, n):
        total += function(a + i * h)  # Add the value at each subinterval

    return total * h  # Multiply by the width to get the integral value

def derivative(point, function):
    """
    A simple numerical derivative using the central difference method.
    
    :param point: The point at which to evaluate the derivative.
    :param function: A callable function to differentiate.
    :return: The approximate value of the derivative at the given point.
    """
    h = 1e-5  # A small number for the difference
    return (function(point + h) - function(point - h)) / (2 * h)  # Central difference formula

def derivation(function):
    """
    A decorator to create a derivative function from a given function.
    
    :param function: A callable function to differentiate.
    :return: A new function that computes the derivative of the original function.
    """
    def derivative_function(point):
        return derivative(point, function)
    
    return derivative_function

def limit(point, function, delta=1e-5):
    """
    A simple numerical limit calculation.
    
    :param point: The point at which to evaluate the limit.
    :param function: A callable function to evaluate the limit of.
    :param delta: A small value to approach the point from both sides.
    :return: The approximate value of the limit at the given point.
    """
    if delta <= 0:
        raise ValueError("Delta must be a positive number.")
    while(function(point - delta) == function(point + delta)):
        delta *= 2
    return (function(point - delta) + function(point + delta)) / 2  # Average from both sides
