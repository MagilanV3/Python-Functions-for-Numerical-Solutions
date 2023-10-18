# This function will return the solution of [A][x] = [b], through 3 methods
# If no method is chosen, it will use numpy.linalg.solve()
# If "inv" is chosen, it will use the inverse method to solve
# If " lu" is chosen, it will use scipy.linalg.lu_solve()

# Import relavent 
import numpy
import scipy
import time

def solve_system(A, b, method=None):
    '''
    (ndarray,ndarry,str)->(ndarray,float)

    , if one
        exists as well as the time taken to find it otherwise None.

    A is a square matrix which is nXn
    b is a column vector so it is nX1
    method is optional and can be :
        inv : for the inverse method
        lu : for the lu decomposition
    '''

    # Start the Timer 
    start = time.time()
    # Check if the matrix [A] is a square matrix
    if numpy.ndim(A) == 2 and numpy.shape(A)[0] != numpy.shape(A)[1]:
        print("Matix [A] is not a square matrix") 
        return None
    # Check if matrix [A] and Vector [B] having matching directions
    if numpy.shape(A)[0] != numpy.shape(b)[0]:
        print("Matix dimension mismatch") 
        return None
    # Check if the system is consistent by checking if rank ([A|B]) = rank(A)
    if numpy.linalg.matrix_rank(A) < numpy.linalg.matrix_rank(numpy.concatenate((A,b), axis=1)):
        print("The system is inconsistent") 
        return None
    # If the "inv" is chosen, then use numpy functions to solve by the inverse method
    if method == "inv":
        final = numpy.dot((numpy.linalg.inv(A)), b)
    # If the "lu" is chosen, then use scipy functions to solve by the LU method
    if method == "lu":
        lu, piv = scipy.linalg.lu_factor(A)
        final = scipy.linalg.lu_solve((lu,piv), b)
    # If the "None" method is chosen, then use numpy built-in function to solve
    if method == None:
        final = numpy.linalg.solve(A,b)

    # Calculate the elapsed time the function takes
    total_time = (time.time()) - start
    return total_time, final

# Solve the first example using method=None
A = numpy.array(
    [[-3, 2, -1],
    [6, -6, 7],
     [3, -4, 4]])
B = numpy.array([[-1],[-7],[-6]])
solution = solve_system(A,B)
print("First example, using method=None")
print("This took " + str(solution[0]) + " seconds")
print("This is the final solution: \n", solution[1])

# Solve the first example using method=lu
solution = solve_system(A,B, method="lu")
print("First example, using method=lu")
print("This took " + str(solution[0]) + " seconds")
print("This is the final solution: \n", solution[1])

# Solve the first example using method=inv
solution = solve_system(A,B, method="inv")
print("First example, using method=inv")
print("This took " + str(solution[0]) + " seconds")
print("This is the final solution: \n", solution[1])

# Solve the second example using method=None
A = numpy.array(
    [[3, 18, 9],
    [2, 3, 3],
     [4, 1, 2]])
B = numpy.array([[18],[117],[283]])
solution = solve_system(A,B)
print("Second example, using method=None")
print("This took " + str(solution[0]) + " seconds")
print("This is the final solution: \n", solution[1])

# Solve the third example using method=None
A = numpy.array(
    [[20, 15, 10],
    [-3, -2.24999, 7],
     [5, 1, 3]])
B = numpy.array([[45],[1.751],[9]])
solution = solve_system(A,B)
print("Third example, using method=None")
print("This took " + str(solution[0]) + " seconds")
print("This is the final solution: \n", solution[1])

