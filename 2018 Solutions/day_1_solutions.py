import csv

#################################################################
######################### Functions #############################

def get_input(input_file_name):
    with open(input_file_name, newline = '') as input_file:
        return [int(row) for row in input_file]

def get_total(input):
    return sum([i for i in input])

def get_first_repeat(input):

    result_set = set({})
    result = 0

    while True:
        for row in input:            
            result += int(row)

            if result in result_set: 
                return result  

            result_set.add(result)

#################################################################

input = get_input('day_1_input.csv')
print(get_total(input))
print(get_first_repeat(input))