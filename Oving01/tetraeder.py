from math import sqrt


def func_a(h):
    a = (3 / sqrt(6))*h
    return a


def func_A(a):
    A = sqrt(3)*a**2
    return A


def func_V(a):
    V = (sqrt(2)*a**3)/12
    return V


# oppgave a
msgA = "Et tetraeder med høyde 3 har areal"
h = 3
a = func_a(h)
A = func_A(a)
print(msgA, round(A, 3))

# oppgave b
msgB = "Et tetraeder med høyde 3 har volum"
V = func_V(a)
print(msgB, round(V, 3))

# oppgave c
inpMsg = "Angi en høyde for trekantene i ditt tetraeder: "
h = float(input(inpMsg))
a = func_a(h)
A = func_A(a)
V = func_V(a)
print(
    f'Ditt tetraeder med høyde {h} har et overflateareal på {A:.3f} og et volum på {V:.3f}')
