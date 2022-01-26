import random
print("Oppgave a)")
def randList(size,lower_bound,upper_bound):
    x = [] 
    for i in range(size):
        x.append(random.randrange(lower_bound,upper_bound+1))
    return x

#testkode oppgave a)
print('size:5, lower:0, upper:5',randList(5,0,5))

print("\nOppgave b)")
def compareLists(list1,list2):
    list = []
    for i in list1:
        for j in list2:
            if i==j: #find duplicates
                if i not in list: #check that dupe isnt in list already
                    list.append(i) #append
    return list

#testkode oppgave b)
list1 = [1,2,2,5]
list2 = [2,4,1,3]
print('Compare lists:',list1,list2,'\nSame nums are:',compareLists(list1,list2))

print("\nOppgave c)")
def multiCompList(lists):
    list = []
    for i in range(len(lists)-1): #compare all lists using nested loop
        for j in range(i,len(lists)): 
            if j != i: # dont check list against itself
                list.append(compareLists(lists[i],lists[j])) #append result of compareList()
    return list

#testkode oppg c)
list3 = [1,5,3,8]
lists = [list1,list2,list3]
print('Comparing list 1, 2 and 3',list1,list2,list3,'\nSame nums in 1v2, 1v3 and 2v3',multiCompList(lists))

print("\nOppgave d)")
def longestEven(list):
    maxLen = 0
    indx = None
    counter = 1
    for i in range(len(list)-1):
        if list[i]%2==0: #even check
            if list[i] == list[i+1]: #check if next num is same
                counter += 1
            else: #reset count on different next num
                counter = 1
            if counter > maxLen: #change of output due to counter
                indx = i-(maxLen-1) #index of sequence start
                maxLen = counter #increments as sequence continues
    return indx, maxLen

#testkode oppgave d)
listE = [1,2,2,7,7,7,7,4,4,4]
print('Longest consecutive sequence of even numbers in:',listE,'\nStart index of sequence and its length:',longestEven(listE))

print('\nmain() included from gitRepo')
def main():
    print(randList(10,2,7))
    a = [1,2,3]
    b = [4,3,1]
    print(compareLists(a,b))
    c = [7,2,1]
    d = [a,b,c]
    print(multiCompList(d))
    liste = [4,3,3,6,2,6,8,3,4,3,3]
    print(longestEven(liste))
main()
