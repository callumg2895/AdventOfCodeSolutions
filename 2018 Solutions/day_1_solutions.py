import csv

#################################################################
## Functions ##

def get_total(input_file_name):
    
    result = 0

    with open(input_file_name, newline = '') as input_file:
        for row in input_file:
            result += int(row)

    return result

def get_first_repeat(input_file_name):

    result_dict = {}
    result = 0
    finished = False

    while not finished:
        with open(input_file_name, newline = '') as input_file:
            for row in input_file:
                
                result += int(row)

                if result in result_dict:
                    finished = True
                    break
                else:
                    result_dict[result] = 0
    
    return result

#################################################################

print(get_total('day_1_input.csv'))
print(get_first_repeat('day_1_input.csv'))