import random

myGuess = random.sample(range(1,34+1),7)

def drawNumbers(list, n):
    results = []
    for i in range(n):
        index = random.randint(0,33-i)
        num = list[index]
        results.append(num)
        list.pop(index)
    return results

def compList(list1, list2):
    dupes = 0 
    for i in list1:
        for j in list2:
            if i == j:
                dupes += 1 # adds 1 if a guessed number is correct
    return dupes

def winnings(x,y):
    out = 0 # if no prize return 0
    if x > 3: # no prize for less then 4 correct
        if x == 7: # lotto for 7 correct
            out = 2749455
        elif x == 6: # 6 correct
            if y > 0: # and 1 or more extra nums
                out = 102110
            else: # and no extra nums
                out = 3385
        elif x == 5: # 5 correct
            out = 95
        elif y > 0: # 4 correct and 1 or more extra nums
            out = 45
    return out

def __main__():
    numbers = list(range(1,34+1)) # make list from 1 to 34
    n_1 = drawNumbers(numbers,10) # draw ten numbers
    x = compList(n_1[:7],myGuess) # splice for: the first 7 numbers
    y = compList(n_1[7:],myGuess) # splice for: 3 extra numbers
    prize = winnings(x,y) # find out if you won
    return prize-5 # return profit, entry costs 5

def spillEnMill():
    globalSum = 0
    for i in range(1000000): # iterate main function a million times
        globalSum += __main__() # add prize-costofentry to sum
    print('Du spiller en million ganger og tjener',globalSum)

print('Du spiller en gang og tjener',__main__())
spillEnMill()

def spillToJackpot():
    z = __main__()
    while z != 2749450:
       z = __main__()
#spillToJackpot()

