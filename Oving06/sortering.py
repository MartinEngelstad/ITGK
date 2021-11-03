print('Oppgave a)')
def bubble_sort(list):
    unsorted = True 
    while unsorted:
        unsorted = False # assume sorted list to break loop if no swaps occur
        for j in range(len(list)-1): # loop over list indices
                if list[j] > list[j+1]: # if current index is large than next
                        list[j], list[j+1] = list[j+1], list[j] #swap
                        unsorted = True #swap happened => list not yet sorted
    return list

#testkode oppg a    
liste = [9,1,34,7,2,3,45,6,78,56,36,65,33,21,23,34,45,6]
print('input list:',liste)
print('output list:',bubble_sort(liste))

print('Oppgave b)')
def selection_sort(list):
    sortedlist = []
    for j in range(len(list)):
        largestNumI = 0
        for i in range(len(list)):
            if list[i] >= list[largestNumI]:
                largestNumI = i
        sortedlist.insert(0,list.pop(largestNumI))  
    return sortedlist

liste = [9,1,34,7,2,3,45,6,78,56,36,65,33,21,23,34,45,6]
print(liste)
print(selection_sort(liste))
