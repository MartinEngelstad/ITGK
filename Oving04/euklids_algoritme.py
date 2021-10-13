print("Euklids algoritme!")

def gcd(a,b):
    while b != 0:
        old_b = b
        b = a % b
        a = old_b
    return a

print("Oppgave a)")
x = 30
y = 10 
print(gcd(x,y))

print("Oppgave b)")
def reduce_fraction(a,b):
    d = gcd(a,b)
    var_a = a/d
    var_b = b/d
    return var_a, var_b

#Testkode for å sjekke at funksjonen din fungerer som den skal
# TESTKODE FOR reduce_fraction
print ("%d/%d" % reduce_fraction (5, 10))
print ("%d/%d" % reduce_fraction (4, 2))
print ("%d/%d" % reduce_fraction (42 , 13))
