import numpy as np 
import matplotlib.pyplot as plt 
import sys


#calculate the two linear regression coefficients
#and also the r2 value
def calculate_linear_regression_coef(x, y): 
	if(np.size(x) != np.size(y)):
 		sys.exit("The two vectors x and y are not of the same length.")

	# number of observations/points 
	n = np.size(x)

	sx = np.sum(x)
	sy = np.sum(y)

	sx2 = np.inner(x,x)
	sxy = np.inner(x,y)
	sy2 = np.inner(y,y)

	# calculating regression coefficients 
	a1 = (n*sxy - sx*sy)/(n*sx2 - sx**2)
	a0 = sy/n - a1*sx/n

	r2 = ((n*sxy-sx*sy)/np.sqrt(n*sx2-sx**2)/np.sqrt(n*sy2-sy**2))**2;

	return(a0, a1, r2) 


#calcuate the coefficients for polynomial regression
#m is the degree of the polynomial.
#returns the coefficient array a for the polynomial
def calculate_poly_regression_coef(x, y, m): 
    if(np.size(x) != np.size(y)):
        sys.exit("The two vectors x and y are not of the same length.")

    # number of observations/points 
    n = np.size(x)
    
    if(n<(m+1)):
        sys.exit("Polynomial regress is impossible because n is less than m + 1.")

    A = np.zeros((m+1,m+1))
    b = np.zeros(m+1)
    
    #loop over each row of matrix A
    for i in range(m+1):
        #loop over each column of current row
        for j in range(m+1):
            if((i+j)==0):
                A[i,j] = n
            else:
                A[i,j] = np.sum(x**(i+j))
                
        if(i==0):
            b[i] = np.sum(y)
        else:
            b[i] = np.inner(x**i, y)
                
    #print(A)
    #print(b)

    # calculating regression coefficients by solving
    # the linear equation system. Here, we call 
    # the solve function in Numpy's linalg package. 
    a = np.linalg.solve(A, b)

    return a

