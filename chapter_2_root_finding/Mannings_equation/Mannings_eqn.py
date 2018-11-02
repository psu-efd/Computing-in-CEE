def secant(f, y0, y1, args):
    eps = args[4]
    f_y0 = f(y0,args)
    f_y1 = f(y1,args)
    iteration_counter = 0
    while abs(f_y1) > eps and iteration_counter < 100:
        try:
            denominator = float(f_y1 - f_y0)/(y1 - y0)
            y = y1 - float(f_y1)/denominator
        except ZeroDivisionError:
            print("Error! - denominator zero for y = ", y)
            sys.exit(1)     # Abort with error
        y0 = y1
        y1 = y
        f_y0 = f_y1
        f_y1 = f(y1,args)
        iteration_counter += 1
    # Here, either a solution is found, or too many iterations
    if abs(f_y1) > eps:
        iteration_counter = -1
    return y, iteration_counter

def f(y,args):
    Q,n,So,B,epsilon = args
    area = B*y 
    wetted_perimeter = B + 2.0*y
    R = area/wetted_perimeter
    residual = Q - 1.0/n*area*R**(2.0/3.0)*So**(0.5)
    return residual


#discharge (m^3/s)
Q=10.0

#Manning's n
n = 0.03

#channel slope
So = 1e-5

#chanenl bottom width - rectangular
B = 10.0

#initial guess of the normal depth (m)
y0 = 1.0
y1 = y0 - 0.1

#accuracy 
eps = 1e-3

# pack all arguments into args0:
# Q, n, So, B, eps
args0 = [Q, n, So, B, eps]	

solution, no_iterations = secant(f, y0, y1, args0)

if no_iterations > 0:    # Solution found
    print("Number of function calls: %d" % (2 + no_iterations))
    print("A solution is: %f" % (solution))
else:
	print("Solution not found!")