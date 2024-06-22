#Bisection method
#0,3,0.001
import math


def volume(h, R):
    return math.pi * h**2 * (3 * R - h) / 3


def bisection_method(R, target_volume, tol=1e-6, max_iter=1000):
    def f(h):
        return volume(h, R) - target_volume


    # Get initial guess values
    a = float(input("Enter the first initial guess (a): "))
    b = float(input("Enter the second initial guess (b): "))


    # Check for valid interval
    if f(a) * f(b) >= 0:
        print("Error: The interval [a, b] does not satisfy f(a) * f(b) < 0.")
        return None


    # Get the tolerance
    tolerance = float(input("Enter the tolerance/error value: "))
    print("step\ta\t\tb\t\tc\t\t0f(c)")


    # Bisection method iterations
    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)


        print(f"{i}\t{a:.7f}\t{b:.7f}\t{c:.7f}\t{fc:.7f}")


        if abs(fc) < tolerance:
            return c


        if f(a) * fc < 0:
            b = c
        else:
            a = c


        if (b - a) < tolerance:
            print("Converged to the tolerance level.")
            return c


    print("Maximum iterations reached. Solution may not be accurate.")
    return None


# Given values
R = 3
target_volume = 30


# Call the bisection method function
result = bisection_method(R, target_volume)


if result is not None:
    print("\nBisection Method Result (h):", result,"m")
