# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?

# Extras:
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num = input('Please input a number ')
num = int(num)
even = f'The number {num} is even'
odd = f'The number {num} is odd'
quad = f'The number {num} is divisible by 4'
if num % 4 == 0:
    print(quad)
elif num % 2 == 0:
    print(even)
else:
    print(odd)
