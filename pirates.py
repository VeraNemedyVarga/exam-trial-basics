pirates = [
    {'Name': 'Olaf', 'has_wooden_leg': False, 'gold': 12},
    {'Name': 'Uwe', 'has_wooden_leg': True, 'gold': 9},
    {'Name': 'Jack', 'has_wooden_leg': True, 'gold': 16},
    {'Name': 'Morgan', 'has_wooden_leg': False, 'gold': 17},
    {'Name': 'Hook', 'has_wooden_leg': True, 'gold': 20},
]

# Write a function that takes any list that contains pirates as in the example,
# And returns a list of names containing the pirates that
# - have wooden leg and
# - have more than 15 gold

def contains_pirates(pirates):
    found_pirates = []
    for pirate_dictionary in pirates:
        if pirate_dictionary['has_wooden_leg'] == True and pirate_dictionary['gold'] > 15:
            found_pirates.append(pirate_dictionary['Name'])
    return found_pirates

print(contains_pirates(pirates))
