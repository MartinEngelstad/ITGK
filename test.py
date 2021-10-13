import random
def bogoSort(a):
    numb = 0
    while (sortCheck(a) == False):
        numb = numb + 1
        shuffle(a)
    print(numb)

def sortCheck(a):
    n = len(a)
    for i in range(0, n-1):
        if (a[i] > a[i+1] ):
            return False
    return True

def shuffle(a):
    n = len(a)
    for i in range (0,n):
        r = random.randint(0,n-1)
        a[i], a[r] = a[r], a[i]
 

a = []
for i in range(10): a.append(random.randint(1, 200))
bogoSort(a)

print("Sorted array :")
for i in range(len(a)):
    print (a[i])
