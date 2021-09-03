def funkA():  # oppgave a
    N_A = 6.022e+23
    stoff = input('Venligst angi navn på stoffet ditt ')
    molvekt = float(input(f'Hva er molvekten til {stoff}? '))
    masse = float(input(f'Hvor mange gram {stoff} har du? '))
    n = masse / molvekt
    x = n * N_A
    print(f'Du har {x:.2e} molekyler {stoff}')


def funkB():  # oppgave b
    melodilinjer = 8.25e+19
    komponertmsg = "Hvor mange ulike ti-toners melodilinjer tror du at du har hørt? "
    komponert = float(input(komponertmsg))
    prosent = (komponert / melodilinjer)*100
    print(
        f"Det var mange... \nmen du har bare hørt {prosent:.2e} prosent av alle mulige melodier!")


# velg oppgave a eller b
def velgOppg():
    valg = input('Ønsker du oppgave a eller b? ')
    if valg == 'a':
        funkA()
    elif valg == 'b':
        funkB()
    else:
        print('Venligst velg enten "a" eller "b"')
        velgOppg()


velgOppg()
