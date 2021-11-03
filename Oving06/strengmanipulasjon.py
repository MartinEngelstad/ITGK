print('Oppgave a)')
def find_substring_indexes(str1,str2):
    str1 = str1.lower()
    str2 = str2.lower()
    list = []
    for i in range(len(str2)): #check all possible starting letters for substrings
        if str1 in str2[i:i+len(str1)]: #if str1 in substring of str2
            list.append(i) #append index of substring
    return list

#testkode oppgave a
str1 = "iS"
str2 = "Is this the real life? Is this just fantasy?"
print(find_substring_indexes(str1,str2))
str1 = "oo"
str2 = "Never let you go let me go. Never let me go ooo"
print(find_substring_indexes(str1,str2))

print('Oppgave b)')
def func(str1,str2,str3):
    str3.lower()
    list = find_substring_indexes(str1,str2) #list of substring indexes
    newStr = ''
    for i in range(len(list)): #replacing same number of substrings as list elmnts
        if i == 0: #for first elmnt, add start of str2, str3 and str2 up to next substring index
            newStr += str2[:list[i]]+str3+str2[list[i]+len(str1):list[i+1]]
        elif i == len(list)-1: #for last element, add str3 and rest of str2
            newStr += str3+str2[list[i]+len(str1):]
        else: #for middle elements, add str3 and str2 up to next substring index
            newStr += str3+str2[list[i]+len(str1):list[i+1]]
    return newStr

#testkode oppgave b            
str1 = "iS"
str2 = "Is this the real life? Is this just fantasy?"
str3 = "cool"
print(f"Substring: {str1}\nwas replaced in: {str2}\nby: {str3}")
print(func(str1,str2,str3),'\n')
str1 = "oo"
str2 = "Never let you go let me go. Never let me go ooo"
str3 = "|replaced|"
print(f"Substring: {str1}\nwas replaced in: {str2}\nby: {str3}")
print(func(str1,str2,str3))