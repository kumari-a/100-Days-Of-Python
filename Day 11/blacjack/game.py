from art import logo
import os
import random
global card , player_point,dealer_point,player_card,dealer_card
cards=[2,3,4,5,6,7,8,9,'K','Q','J','A']
player_point=0
dealer_point=0
player_card=[]
dealer_card=[]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def choice():
    card = random.choice(cards)
    return card

def point_calc(card,player_point):
    if card != 'K' and card != 'Q' and card != 'J' and card != 'A':
        return card
    if card !='A':
        return 10
    if player_point+11<=21:
        return 11
    return 1

def player_play(show):
    clear_console()
    print(logo)
    print('♠️♥️♦️♣Welcome to BlackJack♠️♥️♦️♣️')
    global player_point,player_card
    card = choice()
    player_card.append(card)
    card_points= point_calc(card,player_point)
    player_point+=card_points

    print(f'One of the dealer card is {show}.')

    print('You have the following card ')
    for card in player_card:
        print(card, end=' ')
    print('\n')
    print(f'Your total points is {player_point}.')

    if player_point >21:
        print('Bust out !! You lose 😓')
        return
    more = input("Would you like to draw a card? (y) or would like to pass (p) : ").lower()
    if more == 'y':
        player_play(show)
    elif more == 'p':
        dealer_play()

def dealer_play():
    clear_console()
    print(logo)
    print('♠️♥️♦️♣Welcome to BlackJack♠️♥️♦️♣️')
    global player_point, player_card, dealer_card, dealer_point
    print('You have the following card ')
    for card in player_card:
        print(card, end=' ')
    print('\n')
    print(f'Your total points is {player_point}.')

    print('Dealer has the following card ')
    for card in dealer_card:
        print(card, end=' ')
    print('\n')
    print(f'Dealer has point {dealer_point}')

    if dealer_point == 21:
        print('Dealer got blackjack. You lose! 😓')
        return
    elif dealer_point > 21:
        print("Dealer busts. You Win! 🎇🎆")
    elif dealer_point < 17:
        card = choice()
        dealer_card.append(card)
        card_points = point_calc(card, dealer_point)
        dealer_point += int(card_points)
        dealer_play()
    else:
        if player_point > dealer_point:
            print('You Won! 🎆🎇')
        elif dealer_point > player_point:
            print('Dealer won. 😓')
        else:
            print("It's a draw. 🙄😏")
    return




def main():
    clear_console()
    print(logo)
    global player_point,player_card,dealer_card,dealer_point
    print('♠️♥️♦️♣Welcome to BlackJack♠️♥️♦️♣️')
    for i in range(2):
        card = choice()
        player_card.append(card)
        card_points = point_calc(card,player_point)
        player_point+=card_points

    for i in range(2):
        card = choice()
        dealer_card.append(card)
        card_points = point_calc(card, dealer_point)
        dealer_point += int(card_points)

    print('You have the following card ')
    for card in player_card:
        print(card,end=' ')
    print('\n')
    print(f'Your total points is {player_point}.')

    show = random.choice(dealer_card)
    print(f'One of the dealer card is {show}.')

    if player_point==21:
        print('You got blackjack you won !!! 🎇🎆')
        return

    more = input("Would you like to draw a card? (y) or would like to pass (p) : ").lower()
    if more=='y':
        player_play(show)
    elif more=='p':
        dealer_play()
    else:
        print('Wrong Input')




main()

