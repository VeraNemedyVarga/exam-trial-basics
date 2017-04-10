
def seconds(seconds_list):
    new_list = []
    for element in range(1, len(seconds_list)):
        if element % 2 != 0:
            new_list.append(seconds_list[element])
    return new_list

    # Create a function that takes a list as a parameter,
    # and returns a new list with every second element from the orignal list
    # example: [1, 2, 3, 4, 5] should produce [2, 4]

print(seconds([1, 2, 3, 4, 5, 6])) # should print [2, 4]
