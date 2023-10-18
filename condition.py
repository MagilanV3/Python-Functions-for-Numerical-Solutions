# This function will calculate the the norm of a matrix, which will be used to determine condition number. 

# Important relavent libraries
import numpy as np

# Define Function
def array_norm(M):
    # Check if input is an array
    if (isinstance(M, np.ndarray)) == False:
        print("The input is not an array")
        return None
    # Check if input is square
    elif np.ndim(M) == 2 and np.shape(A)[0] != np.shape(A)[1]:
        print("The Array is not square")
        return None
    # Intialize Variables
    summation = 0
    # Going through each row
    for x in M:
        # Going through each number
        for y in x :
            # Adding every number together
            summation +=(y**2)
    # Square root the sum
    norm = summation**(1/2)
    return norm


#Defining the test-case array
A= np.array([[-3,2,-1],[6,-6,7],[3,-4,4]])

# Finding the norm through the array_norm function 
print(array_norm(A))
# Finding the norm through the builtin function 
print((np.linalg.norm(A)))

# Calculating the matrix condition number through my own method
norm = array_norm(A)
inverse = array_norm(np.linalg.inv(A))
condition = np.dot(norm,inverse)
print(condition)
# Finding the matrix condition number through built in function 
print(np.linalg.cond(A))
