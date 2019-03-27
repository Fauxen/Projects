from Task_2 import *
status_of_items = []
for item in item_numbers:
    # Find index of highest bid for an item according to its position in the item_numbers list.
    index = item_numbers.index(item)
    if highest_bids[index] > reserved_prices[index]:
        status_of_items.append('sold')
    elif number_of_bids[index] > 0:
        status_of_items.append('did not reach reserve price')
    else:
        status_of_items.append('no bids')
print('\nItems sold:-\n')
if 'sold' in status_of_items:
    for status in status_of_items:
        index = status_of_items.index(status)
        if status == 'sold':
            print('Item Number= ' + str(item_number[index]) + '.')
            # Taking total fee by multiplying by 110/100.
            print('Total fee= $' + str((110/100)*highest_bids[index]) + '.\n\n')
else:
    print('None\n\n')
input('Please press enter.')
print('\nItems with bids that did not reach their reserve price: \n')
if 'did not reach reserve price' in status_of_items:
    for status in status_of_items:
        index = status_of_items.index(status)
        if status == 'did not reach reserve price':
            print('Item Number= ' + str(item_number[index]) + '.')
            print('Final bid= $' + highest_bids[index] + '.\n\n')
else:
    print('None\n\n')
input('Please press enter.')
print('\nItems that received no bids: \n')
if 'no bids' in status_of_items:
    for status in status_of_items:
        index = status_of_items.index(status)
        if status == 'no bids':
            print('Item Number= ' + str(item_number[index]) + '.\n')
else:
    print('None\n\n')
input('Please press enter.')
print('\nNumber of items sold= ' + str(status_of_items.count('sold')) + '.')
print('Number of items that did not reach their reserve price= ' + str(status_of_items.count(
    'did not reach reserve price')) + '.')
print('Number of items with no bids= ' + str(status_of_items.count('no bids')) + '.')
