#oppg a
def seperate(numbers,threshold):
    lower = []
    upper = []
    for i in numbers:
        lower.append(i) if i < threshold else upper.append(i)
    return lower, upper

#testkode oppg a
numbers = [1,2,3,4,5,6,7,8,9]
threshold = 5
print('numbers =',numbers)
print('separert ved threshold 5:',seperate(numbers,threshold))

#oppg b
def multiplication_table(n):
    table = []
    for row in range(1,n+1):
        table.append([])
        for col in range(1,n+1):
            table[row-1].append(col*row)
    return table

#testkode oppg b
print('gangetabell opp til 4:',multiplication_table(4))