#Secant Method 
import math


def volume(h, R):
    return math.pi * h**2 * (3 * R - h) / 3


def f(h, R, V):
    return volume(h, R) - V


def df(h, R):
    return 2 * math.pi * h * (3 * R - 2 * h) / 3


def secant_method(R, V, h0, h1, tol=1e-6, max_iter=1000):
    print("\nSecant Method Steps:")
    print("Step\t   Xn-1\t\t  Xn\t\t  Xn+1\t\t  f'(Xn+1)")
    print("----------------------------------------------------------")
   
    h_prev, h = h0, h1
    for i in range(max_iter):
        f_h = f(h, R, V)
        f_prev = f(h_prev, R, V)
        print(f"{i}\t   {h_prev:.7f}\t  {h:.7f}\t  ", end="")
       
        h_new = h - f_h * (h - h_prev) / (f_h - f_prev)
        print(f"{h_new:.7f}\t  {df(h_new, R):.7f}")
       
        if abs(h_new - h) < tol:
            return h_new
       
        h_prev, h = h, h_new
   
    print("Secant method did not converge.")
    return None


# Given values
R = 3
V = 30


# User input for Secant Method
h0_secant = float(input("Enter the first initial guess for Secant Method: "))
h1_secant = float(input("Enter the second initial guess for Secant Method: "))
tolerance_secant = float(input("Enter the tolerance/error value for Secant Method: "))
