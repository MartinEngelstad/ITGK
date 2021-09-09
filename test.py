pos = input('Posisjon: ')

# detirmine position color
# (integer representation of a-h % 2) is same as 1-8 % 2 for black squares


def color():
    if (ord(pos[0].lower()) % 2) == int(pos[1]) % 2:
        print('svart')
    else:
        print('hvit')


if len(pos) != 2:  # user input should not exceed length 2
    print('Feil input. Du må skrive akkurat to tegn')
# check letter and integer of position is within range
elif ord(pos[0].lower()) not in range(97, 104) or int(pos[1]) not in range(1, 8):
    print('Feil input.\nFørste tegn må være en bokstav A-H eller a-h\nAndre tegn må være et tall 1-8')
else:
    color()
    