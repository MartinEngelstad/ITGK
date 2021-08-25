# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras:
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)"
import time
t = time.localtime()
crntYear = int(time.strftime('%Y', t))

print('This Python application calculates in what year you will turn 100!')
name = input('Please enter your name ')
age = int(input('Please enter your age '))
xMsg = int(input('How many times do you wish to se the answer displayed: '))
ansYear = (crntYear - age) + 100
msg = f'Hello {name}! If you are {age} years old right now, you will be 100 years old in {ansYear}! '
for i in range(xMsg):
    print(msg)
