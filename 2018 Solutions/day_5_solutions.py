#################################################################
######################### Functions #############################

def get_input(input_file_name):
    with open(input_file_name, 'r') as input_file:
        return str(''.join(input_file.readlines()))

def different_polarity(item1, item2):
    one_way = (item1.islower() and item2.isupper())
    the_other = (item2.islower() and item1.isupper())
    return one_way or the_other

def same_type(item1, item2):
    return item1.lower() == item2.lower()

def will_react(item1, item2):
    return same_type(item1, item2) and different_polarity(item1, item2)

def react(polymer, delete_type):

    i = 0
    length = len(polymer)

    while i < length:

        if (i == length - 1):
            break
        if same_type(polymer[i], delete_type):
            polymer = (polymer[:(i)] if i > 0 else '')  + (polymer[(i+1):] if i < length - 1 else '')
            length = len(polymer)
            i = max(i-1,0)
        elif will_react(polymer[i], polymer[i+1]):
            polymer = (polymer[:(i)] if i > 0 else '')  + (polymer[(i+2):] if i < length - 2 else '')
            length = len(polymer)
            i = max(i-1,0)
        else:
            i += 1

    # Remove the new line string which was causing an out by one error.
    # ....grumble grumble grumble
    return len(polymer.replace('\n', ''))

def find_shortest_polymer(polymer):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    current_shortest = len(polymer)

    for letter in alphabet:
        current_shortest = min(current_shortest, react(polymer, letter))

    return current_shortest

#################################################################

print(react(get_input('day_5_input.txt'), ''))
print(find_shortest_polymer(get_input('day_5_input.txt')))




