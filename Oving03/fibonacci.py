k = int(input('k: '))
fibonacci = [0,1]
for i in range(2, k):
    n = fibonacci[i-1]+fibonacci[i-2]
    fibonacci.append(n)
out = 0
for n in fibonacci: out += n
print(f'The k first fibonacci numbers are: {fibonacci} \nTheir sum is {out}')

