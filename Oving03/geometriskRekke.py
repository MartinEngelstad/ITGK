r = 0.5
inpN = 4
n = 0
sigma = 0
while n <= inpN:
    sigma += r**n
    n += 1
print(f'Summen av rekken til n = 4 er {sigma}')


tol = 0.001
lim = 1 / (1-r)
n = 0
sigma = 0
while sigma < lim-tol:
    sigma += r**n
    n += 1
print(f'For å være innenfor toleransegrensen: {tol}, kjørte løkken {n} ganger. \nDifferansen mellom virkelig og estimert verdi var da {lim-sigma}')
