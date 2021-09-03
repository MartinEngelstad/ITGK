import sys

inpTask = input('Task a or b ?')

# ask for float input and significant figure
unformattedInpFloat = input('Input your number: ')
inpFloat = float(unformattedInpFloat)
inpSigFig = int(
    input('How many decimals would you like this to be rounded to? '))
# convert to str for string slicing
strInpFloat = str(inpFloat)
decimalIndex = strInpFloat.index('.')

# make list of numbers that are relevant for the upcoming rounding
listForRounding = []
# appending from decimal place "inpSigFig"
if inpSigFig > 0:
    for i in strInpFloat[(decimalIndex+inpSigFig):]:
        listForRounding.append(int(i))
# for 0, append digit to left of decimal and all decimals
elif inpSigFig == 0:
    listForRounding.append(int(strInpFloat[decimalIndex-1]))
    for i in strInpFloat[decimalIndex+1:]:
        listForRounding.append(int(i))
# rounding to nearest 10**(abs(inpSigFig)), example: inpFloat = 35, inpSigFig = -1, rounded number = 40
else:
    for i in strInpFloat[(decimalIndex-1+inpSigFig):(decimalIndex)]:
        listForRounding.append(int(i))

# error for large inpSigFig, prints the users input
if listForRounding == []:
    sys.exit(
        f'(Your input does not have enough decimals to round to that many decimals)\n{unformattedInpFloat}')

# go over listForRounding and round from right to left
for c in range(len(listForRounding)-1):
    endIndex = len(listForRounding)-1
    if (int(strInpFloat[decimalIndex-1]) % 2 != 0):
        if listForRounding[endIndex-c] > 4:
            listForRounding[endIndex-1-c] += 1
            listForRounding[endIndex-c] = 0
    else:
        listForRounding[endIndex-c] = 0

# if only rounding decimals or to zero decimals, keep only rounded digit for output
if inpSigFig > -1:
    roundedListStr = str(listForRounding[0])
# else keep entire list of zeroes for output
else:
    listForRoundingStr = [str(i) for i in listForRounding]
    roundedListStr = ''.join(listForRoundingStr)

# cut the part of the input that wasn't rounded
if inpSigFig > 0:
    restOfFloat = strInpFloat[:inpSigFig+1]
elif inpSigFig == 0:
    restOfFloat = strInpFloat[:decimalIndex-1]
else:
    restOfFloat = strInpFloat[:(decimalIndex-1+inpSigFig)]

# concatenate the strings
roundedNum = restOfFloat + roundedListStr

# output the the rounded number
outputMsg = f'Rounded to {inpSigFig} decimals: '
if inpSigFig > 0:
    print(outputMsg, float(roundedNum))
else:
    print(outputMsg, int(roundedNum))
