navn = input('Hva heter du? ')
#alder = input(f'Hvor gammel er du, {navn}? ')
alder = int(input(f'Hvor gammel er du, {navn}? '))
print(f'Wow, dobbelt så gammel som {alder//2}')
#tid = input('Hva er persen din på 100m? ')
tid = float(input('Hva er persen din på 100m? '))
print(f'{tid}... det var ikke særlig fort')
#tid2 = input('...og på 200m? ')
tid2 = float(input('...og på 200m? '))
rate = tid2 / 19.19
#print('Hmm, på {tid2} kunne UB ha løpt {rate:.2f} 200-metere')
print(f'Hmm, på {tid2} kunne UB ha løpt {rate:.2f} 200-metere')
svar = input(f'OK at han er {rate:.2f}x bedre? ')
