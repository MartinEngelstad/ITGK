from math import sqrt
print("Varierte funksjoner")

print("Oppgave a)")
def divisable(a,b):
    if a % b == 0:
        return True
    else:
        return False

# TESTKODE FOR divisable
print("Er",divisable(10,3), "skal være false")
print("Er",divisable(10,5), "skal være true")


print("Oppgave b)")
def isPrime(a):
    for b in range(2,a):
        if divisable(a,b) == True:
            return False
    return True

# TESTKODE FOR isPrime
print("Er",isPrime(11), "skal være true")
print("Er",isPrime(15), "skal være false")


print("Oppgave c)")
def isPrime2(a):
    if a%2 == 0:
        return False
    i = round(sqrt(a)+0.5)
    for b in range(3,i,2):
        if divisable(a,b) == True:
            return False
    return True 

# TESTKODE FOR isPrime
print("Er",isPrime2(11), "skal være true")
print("Er",isPrime2(15), "skal være false")