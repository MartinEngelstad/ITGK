import math
print("Sekantmetoden!")

print("Oppgave a)")
def f(x):
    return (x-12)*math.e**(x/2)-8*(x+2)**2
def g(x):
    return -x-2*x**2-5*x**3+6*x**4

# testkode for oppgave a
print("f(0) = ", f(0),"  g(1) = ", g(1))


print("Oppgave b)")
def differentiate(x_k, x_k1, func):
    return (func(x_k)-func(x_k1))/(x_k-x_k1)

#testkode oppgave b
print(differentiate(9,10,f))


print("Oppgave c)")
def secant_method(x0,x1,func,tol):
    deltaX = abs(x1-x0)
    while deltaX > tol:
        newX = x0-(func(x0)/differentiate(x0,x1,func))
        deltaX = abs(newX-x0)
        x0 = newX
    return x0
    
#testkode oppgave c
out1 = secant_method(11,13,f,0.00001)
out2 = secant_method(1,2,g,0.00001)
out3 = secant_method(0,1,g,0.00001)
print(f'Funksjonen nærmer seg et nullpkt når x = {round(out1,2)}, da er func(x) = {f(out1):.2e}')
print(f'Funksjonen nærmer seg et nullpkt når x = {round(out2,2)}, da er func(x) = {g(out2):2e}')
print(f'Funksjonen nærmer seg et nullpkt når x = {round(out3,2)}, da er func(x) = {g(out3)}')