# Take a list, say for example this one:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# Extras:
# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

# sol 1:
# for i in a:
#    if i < 5:
#        print(i)

# sol 2:
#msg = 'We have an array and we want to know how much of it you would like to keep, \nEnter a what the largest number you would like to allow into the new array '
#cap = int(input(msg))
#newA = []
# for i in a:
#    if i < cap:
#        newA.append(i)
# print(newA)

# sol 3:
print([aa for aa in a if aa < 5])
# A list behaves as such [output] for [item] in [list] if [filter]
# this means the line is outputting the variable 'aa' which refers to each item in the list 'a'
# Since 'aa refers to each item in the list 'a', the output is each item in the lis, however we have a filter 'if aa < 5'
