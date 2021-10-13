#oppgave a
number_list = []
for i in range(0,100):
    number_list.append(i)
#oppgave b
sum = 0
for i in number_list:
    if i%3==0 or i%10==0:
        sum+=i 
print(sum)
#oppgave c
def swapIndeces(list):
    for i in range(0,100,2):
        list[i], list[i+1] = list[i+1], list[i]
    return list
print(swapIndeces(number_list))
#oppgave d
reversed_list = []
for i in range(1,100):
    reversed_list.append(number_list[-i])
print(reversed_list)