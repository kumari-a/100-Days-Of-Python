import os
from art import logo

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
print(logo)

bids = []

def add_bids(name, bid):
    temp = {
        'bid': bid,
        'name': name
    }
    bids.append(temp)

name = input("What is your name? : ")
bid = int(input("What is your bid? : $"))

while True:
    add_bids(name, bid)
    is_next = input("Are there any other bidders? yes/no: ").lower()
    if is_next == 'yes':
        clear_console()
        name = input("What is your name? : ")
        bid = int(input("What is your bid? : $"))
    else:
        winning_bid = 0
        winner_name = ''
        for bid_info in bids:
            if bid_info['bid'] > winning_bid:
                winning_bid = bid_info['bid']
                winner_name = bid_info['name']
        print(f'Winner is {winner_name} with the bid of ${winning_bid}')
        break
