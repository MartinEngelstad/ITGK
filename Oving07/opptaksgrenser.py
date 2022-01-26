print("Opptaksgrenser!")
print("Oppgave a)")
d = {}
file = open('Oving07/poenggrenser_2011.csv', 'r')
for line in file: # read lines from csv file
    line = line.strip('\n') # strip end
    (key,val) = line.split(',') # create tuple of key and val from line
    d[key] = val # add to dictionary
file.close()

print("Oppgave b)")
def allekominn(dict):
    sum = 0
    for val in dict.values(): 
        if val == 'Alle':
            sum += 1
    return sum
print(allekominn(d))

print("Oppgave c)")
def average(list):
    sum = 0
    for i in list:
        sum += float(i)
    return sum/len(list)

def snittNTNU(dict):
    list = []
    for key,val in dict.items(): 
        if 'NTNU' in key and val != 'Alle':
            list.append(val)
    return average(list)
print(round(snittNTNU(d),3))

print("Oppgave d)")
def lavestInntak(dict):
    # dict.items() to get key:val as list of tuples
    # min of tuples, key kwarg specifies comparison of values in the tuples
    tuple = min(dict.items(), key=lambda x: x[1]) 
    return tuple[0]
print('Studiet med lavest inntak var:',lavestInntak(d))

print("Oppgave e)")
def listOfDicts(dict):
    d = {}
    for key,val in dict.items():
        key = key.split(' ',-1)
        uni = key[0]
        field = key[2]
        try:
            d[uni].append({field:val})
        except:
            d[uni] = [{field:val}]
    return d

def prnt(dict):
    for key,val in dict.items():
        print(key,':\n',val)

#prnt(listOfDicts(d))
