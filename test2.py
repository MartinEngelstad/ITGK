import numpy as np

def f(x):
    y = 6+(1/8)*np.sin(x)
    return y

def f_prime(x):
    y = (1/8)*np.cos(x)-1
    return y

def newton(x_0, iterations):
    for i in range(iterations):
        y = f(x_0)
        y_prime = f_prime(x_0)
        print(x_0,y,y_prime)
        x_0 = x_0 - y/y_prime 
    return x_0

x_0 = 0.37
print(newton(x_0, 3))

def fixed_point(x_0,iterations):
    for i in range(iterations):
        y = f(x_0)
        print(x_0,y)
        x_0 = y
    return x_0

print(round(fixed_point(x_0,9),5))

