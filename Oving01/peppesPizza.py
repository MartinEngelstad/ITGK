pizza = 750
studentrabatt = 0.20
tips = 0.08
subTotal = (pizza*(1-studentrabatt))
totalt = subTotal + (subTotal*tips)

print(
    f'Regning:\nPizza: {pizza} kr\nStudentrabatt: {studentrabatt*100}%\nTips: {tips*100}%\nSum: {totalt} kr')

deltagere = int(input('Hvor mange deltok på middagen? '))
indivPris = round(totalt/deltagere, 2)
print(
    f'Ettersom dere var {deltagere} personer, så må hver person betale {indivPris} kroner.')
