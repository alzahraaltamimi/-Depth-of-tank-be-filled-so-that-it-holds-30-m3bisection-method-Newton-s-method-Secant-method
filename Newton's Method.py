#1
#Newton's Method
import math


def volume(h, R):
    return math.pi * h**2 * (3 * R - h) / 3


def f(h, R, V):
    return volume(h, R) - V


def df(h, R):
    return 2 * math.pi * h * (3 * R - 2 * h) / 3


def newtons_method(R, V, h0, tol=1e-6, max_iter=1000):
    print("\nNewton's Method Steps:")
    print("Step\tXn\t\tf(Xn)\t\tf'(Xn)\t\t  Xn+1")
    print("-------------------------------------------------------------------")
   
    h = h0
    for i in range(max_iter):
        f_h = f(h, R, V)
        df_h = df(h, R)
        print(f"{i}\t{h:.7f}\t{f_h:.7f}\t{df_h:.7f}\t  ", end="")
       
        h_new = h - f_h / df_h
        print(f"{h_new:.7f}")
       
        if abs(h_new - h) < tol:
            return h_new
       
        h = h_new
   
    print("Newton's method did not converge.")
    return None


# Given values
R = 3
V = 30


# User input for Newton's Method
h0_newton = float(input("Enter the first initial guess for Newton's Method: "))
tolerance_newton = float(input("Enter the tolerance/error value for Newton's Method: "))


# Newton's Method
newton_result = newtons_method(R, V, h0_newton, tolerance_newton)
if newton_result is not None:
    print("\nNewton's Method Result (h):", newton_result,"m")
