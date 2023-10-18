# This will solve the root of a function using the Newton-Raphson Method
# If the dervivative is not given, it will use the Secant method to obtain the value

# Declare the function 
f = lambda x : x**5 - 11*x**4 + 43*x**3 - 73*x**2 + 56*x -16 # define function
fp = lambda x : 5*x**4 - 44*x**3 + 129*x**2 - 146*x + 56

# Define Function and variables
def myNR(myfun, x0, myfund=None):
    # Intialize the variables used
    iteration_count = 0 
    tolerance = 1
    old_guess = x0
    secant_method = myfund
    # Begin a while loop that remains true until the approximate relative error is 10*-6
    # The loop will also break if it goes past 100 iterations, in case there it doesn't converge
    while tolerance > 1e-6 and iteration_count != 101:
        # If there is no myfund value given then use the secant method to calculate the dervivate value
        if secant_method==None:
            myfund_value = ((myfun(old_guess*1.01)) - (myfun(old_guess))) / ((old_guess*1.01) - old_guess) 
        else:
            # If myfund is given, then use the function to obtain the value 
            myfund_value = myfund(old_guess)
        iteration_count +=1
        # Employ the Newton Raphson method to get a new guess
        new_guess = old_guess - ((myfun(old_guess)) / (myfund_value)) 
        # Find out the approximate relative error
        tolerance = abs((old_guess - new_guess) / old_guess)
        old_guess = new_guess
            
    return new_guess

if __name__ == "__main__":

    print("This is the root: " + str(myNR(f, -2)))
