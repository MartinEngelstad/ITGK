import random

a = int(input('a: '))
b = int(input('b: '))
tilfeldigTall = random.randint(a,b)
ans = int(input('Gjett: '))
while ans != tilfeldigTall:
    if ans < tilfeldigTall:
        print('Tallet er høyere')
    else:
        print('Tallet er lavere')
    ans = int(input('Gjett: '))
print('Du gjettet riktig!')