import time
import Task_1
highest_bids = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
buyer_numbers = {'1256': 'bidding', '2301': 'bidding', '2244': 'bidding', '8976': 'bidding', '9009': 'bidding',
                 '8221': 'bidding'}
print('\nWelcome to the Auction!\n\nChoose from the items below:\n')


def print_items():
    for item_number in Task_1.item_numbers:
        print('Item Number= ' + str(item_number) + '.')
        # Find the index of item_number in the list and use that to find index of description.
        print('Item Description= ' + Task_1.descriptions[Task_1.item_numbers.index(item_number)])
        print('Current Highest Bid= $' + str(highest_bids[Task_1.item_numbers.index(item_number)]) + '.\n\n')


while 1:
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
                    time.sleep(1)
                    # We check if everyone has said no.
                    if 'bidding' not in buyer_numbers.values():
                        break
                    else:
                        continue
                else:
                    item_number = int(input('\nPlease enter the item number: '))
                    if item_number in Task_1.item_numbers:
                        bid = int(input('\nPlease enter your bid: $'))
                        # Find index of item_number in the item_numbers list then use the index to get highest_bid.
                        if bid > highest_bids[Task_1.item_numbers.index(item_number)]:
                            highest_bids[Task_1.item_numbers.index(item_number)] = bid
                            Task_1.number_of_bids[Task_1.item_numbers.index(item_number)] += 1
                            print('\nBid successful. Thank you!')
                            time.sleep(2)
                        else:
                            print('\nWe are sorry, but your bid is too low.')
                            time.sleep(2)
                    else:
                        print('\nWe are sorry, but there is no such item number.\n')
                        time.sleep(2)
            else:
                print('\nWe are sorry, but you are not authorized to bid.\n')
                time.sleep(2)
        else:
            print('\nPlease input a valid option.\n')
            time.sleep(2)
    except ValueError:
        print("\nIncorrect input.")
        time.sleep(2)
print('\nThe auction has come to an end. Thank you everyone!\n')