# This Python script solves an Ax = b problem, using the Guass-Seidel Method

# Import Relavent Libraries
import numpy as np

# Define the A matrix and b array
a=np.array([[0.2425,0,-0.9701],[0,0.2425,-0.9701],[-0.2357,-0.2357,-0.9428]])
b=np.array([247,248,239])

# Define the initial guesses
guess = np.array([10., 10., 10.])

def guass(a, b , guess):
    # Intialize relavent variables
    count = 0 
    error = 1.
    current_guess = guess
    prev_guess = current_guess.copy()
    diagonal_count = 0
    # Check if the matrix is diagonally dominant
    for x in a:
        if x[diagonal_count] != np.max(x):
                print("Matrix [A] is not Diagonally Dominant")
                return None
        else:
                diagonal_count += 1
    # This loop will iterate using the Guass-Seidel method the until the relative error is greater than 10*-6
    # This loop will also break if it goes past 100 iteration, in the case that there is no convergence
    while error > 1.e-6 and count != 101:
        # Loop through each row of the matrix
        for x in range(len(a)):
            total = 0
            # Loop through each value in the row
            for y in range(len(a)):
                if x!=y:
                    # This will calcualte a part of the numerator used to calculate the next guess
                    total = (a[x,y]*current_guess[y]) + total
            # This will calculate the new guess 
            current_guess[x] = (total-b[x]) / (-(a[x,x]))
        # Calculate the new error
        error = sum(abs(prev_guess - current_guess))
        prev_guess = current_guess
        count +=1
    return current_guess

print(guass(a,b,guess))

# However, using the GS method, I can say that there isn’t convergence as the matrix “A” is not diagonally dominant. 
# This is confirmed by my code’s output when checking for diagonally dominance. 