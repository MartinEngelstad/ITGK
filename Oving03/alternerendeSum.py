n = int(input('n: '))
out = 1
for i in range(2, n+1):
    out = (out - i**2) if (i % 2) == 0 else (out + i**2)  
    print(i,out)
print(f'The sum of the series to the n-th iteration: {out}')

k = int(input('k: '))
out = 1
i = 1
while k >= out:
    i += 1
    newOut = (out - i**2) if (i % 2) == 0 else (out + i**2)
    if newOut > k:
        break
    else:
        out = newOut
        
print(f'The sum before the sum becomes larger than k is {out}. This is on iteration: {i-1}')