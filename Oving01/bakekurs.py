import copy

baseCookieNr = 48
sweet = False
printWidth = 20
# list of ingredients
ingredients = []


# creating class for an ingredient
class ingredient:
    def __init__(ingredient, name, amount):
        ingredient.name = name
        ingredient.amount = amount


# appending ingredients
ingredients.append(ingredient('sukker(g)', 400.0))
ingredients.append(ingredient('smør(g)', 320.0))
ingredients.append(ingredient('sjokolade(g)', 500.0))
ingredients.append(ingredient('egg', 2.0))
ingredients.append(ingredient('hvetemel(g)', 460.0))


# function for printing a list of ingredients, either vertically or in table for task b
def printIngredients(list):
    for i in list:
        print(i.name, i.amount, sep=': ')


def printSweet(adjustedRecipe, num):
    sugarAmount = adjustedRecipe[0].amount
    chocoAmount = adjustedRecipe[2].amount
    print(f'{num}{str(sugarAmount).rjust(printWidth+11)}{str(chocoAmount).rjust(printWidth)}')


# function that takes a desired cookie amount and adjusts the amount of ingredients
# vairable sweet determines print function used
def adjustRecipe(desiredCookieAmount):
    ratio = desiredCookieAmount/baseCookieNr
    adjustedRecipe = []
    for i in ingredients:
        newIngredient = copy.copy(i)
        newIngredient.amount = round(i.amount * ratio, 2)
        adjustedRecipe.append(newIngredient)
    if sweet != True:
        printIngredients(adjustedRecipe)
    else:
        printSweet(adjustedRecipe, desiredCookieAmount)


# oppgave a
cookieBakeMsg = 'Hvor mange cookies ønsker du å bake? '
adjustRecipe(int(input(cookieBakeMsg)))

# oppgave b
# set sweet to True so that adjustRecipe() changes print function
# ask for 3 amounts of cookies
sweet = True
print('Du skal lage tre batches med cookies:')
num1 = int(input(cookieBakeMsg))
num2 = int(input(cookieBakeMsg))
num3 = int(input(cookieBakeMsg))

# header for the table of required sukker(g) and sjokolade(g) amounts
headerString1 = 'Antall cookies:'
headerString2 = '     sukker (g)'
headerString3 = '  sjokolade (g)'
print(f'{headerString1}\t{headerString2.rjust(printWidth)}\t{headerString3.rjust(printWidth)}')

# adjust recipe for the three cookie amounts
adjustRecipe(num1)
adjustRecipe(num2)
adjustRecipe(num3)
