from os import system, name
from time import sleep
from Task_1 import *
highest_bids = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
buyer_numbers = {'1256': 'bidding', '2301': 'bidding', '2244': 'bidding'}
print('\nWelcome to the Auction!\n')
input('Press enter to continue')


def print_items():
    for item_number in item_numbers:
        print('\nChoose from the items below:\n\n')
        print('Item Number= ' + str(item_number) + '.')
        # Find the index of item_number in the list and use that to find index of description.
        index = item_numbers.index(item_number)
        print('Item Description= ' + descriptions[index])
        print('Current Highest Bid= $' + str(highest_bids[index]) + '.\n\n')


def clear():
    """For clearing the screen after printing items."""
    if name == 'nt':
        system('cls')
    else:
        system('clear')


while 1:
    clear()
    print_items()
    try:
        prompt = input('Do you want to place a bid? [yes/no]: ')
        # The auction ends when all the buyers say no.
        if prompt == 'no' or prompt == 'yes':
            buyer_number = input('\nPlease enter your buyer number: ')
            if buyer_number in buyer_numbers and buyer_numbers[buyer_number] == 'bidding':
                # Now we check if he had said no.
                if prompt == 'no':
                    buyer_numbers[buyer_number] = 'not bidding'
                    print('\nThank you!')
                    sleep(1)
                    # We check if everyone has said no.
                    if 'bidding' not in buyer_numbers.values():
                        break
                    else:
                        continue
                else:
                    item_number = int(input('\nPlease enter the item number: '))
                    if item_number in item_numbers:
                        bid = int(input('\nPlease enter your bid: $'))
                        # Find index of item_number in the item_numbers list then use the index to get highest_bid.
                        if bid > highest_bids[item_numbers.index(item_number)]:
                            highest_bids[item_numbers.index(item_number)] = bid
                            number_of_bids[item_numbers.index(item_number)] += 1
                            print('\nBid successful. Thank you!\n')
                            sleep(2)
                        else:
                            print('\nWe are sorry, but your bid is too low.')
                            sleep(2)
                    else:
                        print('\nWe are sorry, but there is no such item number.\n')
                        sleep(2)
            else:
                print('\nWe are sorry, but you are not authorized to bid.\n')
                sleep(2)
        else:
            print('\nPlease input a valid option.\n')
            sleep(2)
    except ValueError:
        print("\nIncorrect input.")
        sleep(2)
print('\nThe auction has come to an end. Thank you everyone!')
sleep(2)
