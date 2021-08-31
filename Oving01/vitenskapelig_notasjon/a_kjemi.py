N_A = 6.022e+23
nuklide = input('Venligst angi navn på stoffet ditt ')
molvekt = float(input(f'Hva er molvekten til {nuklide}? '))
masse = float(input(f'Hvor mange gram {nuklide} har du? '))
n = masse / molvekt
x = n * N_A
print(f'Du har {x:.2e} molekyler {nuklide}')
