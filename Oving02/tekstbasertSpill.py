prompt = 'What will you do? '
inpErr = 'This is not a supported command'
gameIntro = 'You awake on a cold cobblestone floor. The air is damp and your head aches as you sit up in your cell.\nA cold breeze whisps through the window and the metal bars of the door creak as a guard passes by with todays breakfast.'
print(gameIntro)
choice01 = input(prompt).lower()

if choice01 == 'open door' or choice01 == 'try door':
    print('The door is locked')
elif choice01 == 'jump out window' or choice01 == 'climb out window':
    print('You fall to your death')
elif choice01 == 'eat breakfast' or choice01 == 'eat food':
    print('You retrieve the stale bread and water laying outside the barred door, it is better than nothing, you think as you eat your breakfast')
else:
    print(inpErr)
