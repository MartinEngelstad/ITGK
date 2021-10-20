print("Not quite Blackjack!\n")
import random

cards = ["a",2,3,4,5,6,7,8,9,10,10,10,10]
anotherQuery = 'Do you want another card? (J/N) '

def hit():
    x = cards[random.randint(0,len(cards)-1)]
    return x

def aceSum(hand,y):
    hand_sum = 0
    for i in hand:
        if i == 'a':
            hand_sum += y
        else:
            hand_sum += i
    return hand_sum

def hand_sum(hand):
    hand_sum = 0
    for i in hand:
        if i == 'a':
            oneSum = aceSum(hand,1)
            elevenSum = aceSum(hand,11)
            if oneSum % 21 > elevenSum % 21:
                i = 1
            else:
                i = 11
        hand_sum += i
    return hand_sum

def reveal(playerHand):
    dealerSum = hand_sum(dealerHand)
    playerSum = hand_sum(playerHand)
    print(f'Dealers score: {dealerSum} \nPlayer score: {playerSum}')
    if dealerSum > playerSum:
        print('You loose.')
    elif dealerSum < playerSum:
        print('You win!')
    else:
        print("It's a tie!")   

def choice(playerHand):
    inpChoice = input(anotherQuery)
    if inpChoice == 'J':
        handSum = hand_sum(playerHand)
        playerHand = [handSum]
        playerHand.append(hit())
        newSum = hand_sum(playerHand)
        print(f'Your new sum is {newSum}')
        if newSum > 21:
            print('Bust!')
        else:   
            choice(playerHand)
    else:
        reveal(playerHand)

def checkBlackJack(hand):
    if (hand[0] == 'a') and (hand[1] == 10):
        return True
    if (hand[1] == 'a') and (hand[0] == 10):
        return True
    else:
        return False

#Start of game
playerHand = [hit(),hit()]
dealerHand = [hit(),hit()]

if checkBlackJack(dealerHand) and checkBlackJack(playerHand):
    print("Both BlackJack! Tie")
elif checkBlackJack(dealerHand):
    print('Dealer blackjack, you lose.')
elif checkBlackJack(playerHand):
    print("BlackJack! You win")
else:
    print(f'Dealer cards are {dealerHand[0]} and ?')
    print(f'Your hand: {playerHand} Your sum: {hand_sum(playerHand)}')
    choice(playerHand)
    
        
