# Ulik lengde på dataene gjør utskrift av flere rader rotete:
print('DELTAKER', 'Oppg1', 'Oppg2')
print('Ada', 18, 125.75)
print('Augustus', 104, 15.4)

# Med fstring kan vi angi format med : inni { }
print(f'{"DELTAKER":<15} {"Oppg1":>6} {"Oppg2":>8}')
navn, pt1, pt2 = 'Ada', 18, 125.75
print(f'{navn:<15} {pt1:6} {pt2:8.2f}')
navn, pt1, pt2 = 'Augustus', 104, 15.4
print(f'{navn:<15} {pt1:6} {pt2:8.2f}')

# Forklaring: Tallet bak kolon angir feltbredde
# Kan dermed sikre uniform bredde på hver kolonne
# For tekst kan dessuten angis justering:
#    < venstre, > høyre, ^ midt
# For float kan angis to tall: bredde.desimaler
# etterfulgt av bokstaven f (hvis vi dropper denne,
# vil desimaltall komme ut i vitenskapelig notasjon)
