print("Tallak!")

print("Oppgave a)")
def number_of_lines(filename):
    f = open(filename,'r')
    num = 0
    for line in f:
        num += 1
    f.close()
    return num

print(number_of_lines('Oving07/numbers.txt'))

print("Oppgave b)")
def number_frequency(filename):
    d = {}
    f = open(filename,'r')
    for line in f:
        num = int(line.strip('\n'))
        try:
            d[num] += 1
        except:
            d[num] = 1
    f.close()
    return d

print(number_frequency('Oving07/numbers.txt'))

print("Oppgave c)")
d = number_frequency('Oving07/numbers.txt')
for key,val in d.items():
    print(str(key)+':',val)