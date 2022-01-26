print("Søke i tekst!")

print("Oppgave a)")
def read_from_file(filename):
    f = open(filename,'r')
    content = f.read()
    f.close()
    return content

content = read_from_file('Oving07/alice_in_wonderland.txt')
#print(content)

print("Oppgave b)")
def remove_symbols(text):
    text = text.lower()
    newTxt = ''
    for i in text:
        if i.isalpha() or i == ' ': # or i == '\n' (for legebility)
            newTxt += i      
    return newTxt

newTxt = remove_symbols(content)
#print(newTxt)

print("Oppgave c)")
def countWords(filename):
    content = read_from_file(filename)
    pureTxt = remove_symbols(content)
    d = {}
    l = pureTxt.split(' ',-1)
    for i in l:
        try:
            d[i] += 1
        except:
            d[i] = 1
    return d

print("Oppgave d)")
wordCountDict = countWords('Oving07/alice_in_wonderland.txt')
sum = 0
for word,val in wordCountDict.items():
    #print(word,val)
    sum += val
print(sum)
