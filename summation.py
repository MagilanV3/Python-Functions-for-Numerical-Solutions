# Summation from n=0 to infinty, for x^^n
# This is only defined for when the absolute of x is less than 1.

def summation(x, tolerance=1e-5):
    # Checking if the value is in betwen the range of (-1, 1) 
    if abs(x) >= 1:
        raise ValueError ("x must be in the range (-1, 1).")

    #Defining Relavent variables
    result = 0
    term = 1
    n = 0

    #Running the Summation until the tolerance is met
    while abs(term) > tolerance:
        result += term
        n += 1
        term = x**n
    return result
