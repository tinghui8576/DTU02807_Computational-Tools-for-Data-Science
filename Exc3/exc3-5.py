from functools import reduce

with open("data/friends.txt", 'r') as file:
    t = file.read()

l = map(lambda x, y: (x, y), my_strings, my_numbers)