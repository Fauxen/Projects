from Task_2 import *
status_of_items = []
total_auction_fee = 0
for item in item_numbers:
    # Find index of highest bid for an item according to its position in the item_numbers list.
    index = item_numbers.index(item)
    if highest_bids[index] > reserved_prices[index]:
        status_of_items.append('sold')
    elif number_of_bids[index] > 0:
        status_of_items.append('did not reach reserve price')
    else:
        status_of_items.append('no bids')
if 'sold' in status_of_items:
    index_start = 0
    for status in status_of_items:
        index = status_of_items.index(status, index_start)
        if status == 'sold':
            # Taking total fee by multiplying by 110/100, then round it to cents.
            total_auction_fee += round((10/100)*highest_bids[index], 2)
        index_start += 1
    print('\nTotal auction fee= $' + str(total_auction_fee) + '\n\n')
else:
    print('Total auction fee= $0')
input('Press enter to continue')
print('\nItems with bids that did not reach their reserve price:- \n')
if 'did not reach reserve price' in status_of_items:
    index_start = 0
    for status in status_of_items:
        index = status_of_items.index(status, index_start)
        if status == 'did not reach reserve price':
            print('Item Number= ' + str(item_numbers[index]) + '.')
            print('Final bid= $' + str(highest_bids[index]) + '.\n\n')
        index_start += 1
else:
    print('None\n\n')
input('Press enter to continue')
print('\nItems that received no bids:- \n')
if 'no bids' in status_of_items:
    index_start = 0
    for status in status_of_items:
        index = status_of_items.index(status, index_start)
        if status == 'no bids':
            print('Item Number= ' + str(item_numbers[index]) + '.\n')
        index_start += 1
else:
    print('None\n\n')
input('Press enter to continue')
print('\nNumber of items sold= ' + str(status_of_items.count('sold')) + '.')
print('Number of items that did not reach their reserve price= ' + str(status_of_items.count(
    'did not reach reserve price')) + '.')
print('Number of items with no bids= ' + str(status_of_items.count('no bids')) + '.\n')
