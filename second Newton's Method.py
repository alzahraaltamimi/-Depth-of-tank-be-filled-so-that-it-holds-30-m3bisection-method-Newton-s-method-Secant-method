
# new Newton's Method

# import math


def volume(h):
    return (h**2)-(2*h)-35 


def f(h):
    return volume(h) 


def df(h):
    return 2 * (h**2)-(2*h)-35


def newtons_method( h0, tol=1e-6, max_iter=1000):
    print("\nNewton's Method Steps:")
    print("Step\tXn\t\tf(Xn)\t\tf'(Xn)\t\t  Xn+1")
    print("-------------------------------------------------------------------")
   
    h = h0
    for i in range(max_iter):
        f_h = f(h)
        df_h = df(h)
        print(f"{i}\t{h:.7f}\t{f_h:.7f}\t{df_h:.7f}\t  ", end="")
       
        h_new = h - f_h / df_h
        print(f"{h_new:.7f}")
       
        if abs(h_new - h) < tol:
            return h_new
       
        h = h_new
   
    print("Newton's method did not converge.")
    return None

# Given values
#none 
# User input for Newton's Method
h0_newton = float(input("Enter the first initial guess for Newton's Method: "))
tolerance_newton = float(input("Enter the tolerance/error value for Newton's Method: "))


# Newton's Method
newton_result = newtons_method( h0_newton, tolerance_newton)
if newton_result is not None:
    print("\nNewton's Method Result (h):", newton_result,"m")
    
    
