# fizzbuzz
# if print int from 1 to 100,
# if divisible by 3 print fizz,
# if divisible by 5 pring buzz,
# if both print fizzbuzz

for x in range(1, 100):
    output = ''
    if x % 3 == 0:
        output += 'fizz'
    elif x % 5 == 0:
        output += 'buzz'
    elif x % 7 == 0:
        output += 'ruzz'
    else:
        output = x
    print(output)
