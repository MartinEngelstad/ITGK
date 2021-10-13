print("Matrisemultiplikasjon!")
import random
def random_matrise(bredde,hoyde):
    matrise = []
    for i in range(bredde):
        matrise.append([])
        for j in range(hoyde):
            matrise[i].append(random.randint(0,10))
    return matrise

def print_matrise(matrise,navn):
    print(navn,'=[')
    for i in matrise:
        print(i)
    print(']')

def matrise_addisjon(x,y):
    if len(x) != len(y):
        print('Matrisene er ikke av samme dimensjon')
    else:
        matrise = []
        for i in range(len(x)):
            matrise.append([])
            for j in range(len(x[i])):
                matrise[i].append(x[i][j]+y[i][j])
        return matrise

#Kjør main for å sjekke at du har løst oppgaven riktig. 
def main():
    A = random_matrise(4,3)
    print_matrise(A, 'A')
    B = random_matrise(3,4)
    print_matrise(B, 'B')
    C = random_matrise(3,4)
    print_matrise(C, 'C')
    D = matrise_addisjon(A,B)
    E = matrise_addisjon(B,C)
    print_matrise(E, 'B+C' )

main()