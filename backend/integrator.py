def linear_function(x):
    y = 0
    for i in range(2):
        y += x**i
    return y

result =  linear_function("p")
print(result)

def polynomial_function(x, n):
    """
    A simple polynomial function that sums powers of x up to n.
    :param x: The input value.
    :param n: The highest power of x to include in the sum.
    :return: The sum of powers of x from 0 to n.
    """
    y = 0
    for i in range(n + 1):
        y += x**i
    return y



def function(x, y): #definded what a function is
    for i in range(0,n):
        y += x**i
    y = function(x)
    return y
    

# def sequence(x, n):
#     function(x) = x(i)
#     if n <= 0:
#         raise ValueError("n must be a positive integer.")
#     for i in range(n):
#         if x(i+1) - x(i) == x(i+2) - x(i+1):
#             x(i+1) = x(i) + (x(i+2) - x(i+1))
#         elif x(i+1)/x(i) == x(i+2)/x(i+1):
#             x(i+1) = x(i) * (x(i+2)/x(i+1))
#         else:
#             raise ValueError("The sequence is not arithmetic or geometric.")
#     return function


# def check_for_sequence(function):
#     n = 1
#     while n<1:
#         print("Please enter a valid sequence")
#         n = int(input("Enter a positive integer for the sequence length: "))
#     return [sum(function(i)) for i in range(n)]


# def summation(interval,function):
#     """
#     A simple numerical summation using the trapezoidal rule.
#     :param interval: A tuple (a, b) representing the interval of summation.
#     :param function: A callable function to sum over the interval.
#     :return: The approximate value of the summation.
#     """
#     a, b = interval
#     n = 1000  # Number of subintervals
#     h = (b - a) / n  # Width of each subinterval
#     total = 0.5 * (function(a) + function(b))  # Start with the endpoints
#     for i in range(1, n):
#         total += function(a + i * h)  # Add the value at each subinterval
#     return total * h    


# def integration(interval, function):
#     """
#     A simple numerical integration using the trapezoidal rule.
    
#     :param interval: A tuple (a, b) representing the interval of integration.
#     :param function: A callable function to integrate.
#     :return: The approximate value of the integral.
#     """
#     a, b = interval
#     n = 1000  # Number of subintervals
#     h = (b - a) / n  # Width of each subinterval
#     total = 0.5 * (function(a) + function(b))  # Start with the endpoints

#     for i in range(1, n):
#         total += function(a + i * h)  # Add the value at each subinterval

#     return total * h  # Multiply by the width to get the integral value

# def derivative(point, function):
#     """
#     A simple numerical derivative using the central difference method.
    
#     :param point: The point at which to evaluate the derivative.
#     :param function: A callable function to differentiate.
#     :return: The approximate value of the derivative at the given point.
#     """
#     h = 1e-5  # A small number for the difference
#     return (function(point + h) - function(point - h)) / (2 * h)  # Central difference formula

# def derivation(function):
#     """
#     A decorator to create a derivative function from a given function.
    
#     :param function: A callable function to differentiate.
#     :return: A new function that computes the derivative of the original function.
#     """
#     def derivative_function(point):
#         return derivative(point, function)
    
#     return derivative_function

# def limit(point, function, delta=1e-5):
#     """
#     A simple numerical limit calculation.
    
#     :param point: The point at which to evaluate the limit.
#     :param function: A callable function to evaluate the limit of.
#     :param delta: A small value to approach the point from both sides.
#     :return: The approximate value of the limit at the given point.
#     """
#     if delta <= 0:
#         raise ValueError("Delta must be a positive number.")
#     while(function(point - delta) == function(point + delta)):
#         delta *= 2
#     return (function(point - delta) + function(point + delta)) / 2  # Average from both sides
