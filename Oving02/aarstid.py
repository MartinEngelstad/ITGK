inpMonth = input('Måned: ')
inpDay = int(input('Dag: '))

#om en måned som kun befinner seg i en årstid
if inpMonth == 'april' or inpMonth == 'mai':
    print('Vår')
elif inpMonth == 'juli' or inpMonth == 'august':
    print('Sommer')
elif inpMonth == 'oktober' or inpMonth == 'november':
    print('Høst')
elif inpMonth == 'januar' or inpMonth == 'februar':
    print('Vinter')
#om måned i to årstider -> før eller etter dato?
elif inpMonth == 'mars':
    if inpDay < 20:
        print('Vinter')
    else:
        print('Vår')
elif inpMonth == 'juni':
    if inpDay < 21:
        print('Vår')
    else:
        print('Sommer')
elif inpMonth == 'september':
    if inpDay < 22:
        print('Sommer')
    else:
        print('Høst')
elif inpMonth == 'desember':
    if inpDay < 21:
        print('Høst')
    else:
        print('Vinter')
