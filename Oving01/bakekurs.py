import copy

baseCookieNr = 48
sweet = False
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


# function for printing a list of ingredients
def printIngredients(list):
    for i in list:
        print(i.name, i.amount, sep=': ')


# function that prints a table of the required sukker(g) and sjokolade(g) to make the amount of cookies aquired from input
sugarIndex = 1


def printSweet(adjustedRecipe, num):
    print(
        f'{str(num).rjust(5)}\t{adjustedRecipe[0].amount:25.2f}\t{adjustedRecipe[2].amount:.2f}')


# prints the basic recipe for 48 cookies
# printIngredients(ingredients)

# function that takes a desired cookie amount and adjust the amount of ingredients
# for oppgave a sweet = False, and the recipe is printed in the standard conifuguration


def adjustRecipe(desiredCookieAmount):
    ratio = desiredCookieAmount/baseCookieNr
    adjustedRecipe = []
    for i in ingredients:
        newIngredient = copy.copy(i)
        newIngredient.amount = i.amount * ratio
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
headerString2 = 'sukker (g)'
headerString3 = 'sjokolade (g)'
print(f'{headerString1}{headerString2.rjust(20)}\t{headerString3}')

# adjust recipe for the three cookie amounts
adjustRecipe(num1)
adjustRecipe(num2)
adjustRecipe(num3)
