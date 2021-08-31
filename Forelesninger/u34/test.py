# a = float(input('Input en verdi for a '))
a = 2.5
b = a
c = a + b
b = 1.5
#print(f'a: {a:<10}, b: {b:^10}, c: {c:<10}')

dicT = {}

dicT['pils'] = "pompe"

dicT['manual'] = {}

dicT['manual']['how2pompe'] = "FØLG BRUKSANVISNINGEN"

for key, value in dicT.items():
    print("key: ", key, '\n', "value: ", value)
    if type(key) is dict:
        for key, value in dicT[key].items():
            print("key: ", key, '\n', "value: ", value)
