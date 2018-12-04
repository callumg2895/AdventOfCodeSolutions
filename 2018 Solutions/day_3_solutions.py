import csv

#################################################################
######################### Variables #############################

grid = [['0' for i in range(1000)] for i in range(1000)]
id_list = []
claims_dict = dict({})

#################################################################
######################### Functions #############################

def get_input(input_file_name):
    with open(input_file_name, newline = '') as input_file:
        for row in input_file:

            item = str(row).strip('\r\n').replace('#', '').replace(' @ ', ' ').replace(',', ' ').replace(': ', ' ').replace('x', ' ').split(' ')
             
            id_list.append(item[0])
            claims_dict[item[0]] = [int(item[1]), int(item[2]), int(item[3]), int(item[4])]


def add_claims(ids):

    while len(ids) > 1:
        for id in ids:
            if add_claim(id):
                ids.remove(id)

    return ids[0]            

def add_claim(id):

    claim = claims_dict[id]
    overlaps = False

    x_start = claim[0]
    y_start = claim[1]
    x_max = x_start + claim[2]
    y_max = y_start + claim[3]

    for x in range(x_start, x_max):
        for y in range(y_start, y_max):

            if grid[x][y] == '0' or grid[x][y] == id:
                grid[x][y] = id
            else:
                overlaps = True
                grid[x][y] = 'X'

    return overlaps

def count_conflicts():

    result = 0

    for x in range(1000):
        for y in range(1000):
            result += 1 if grid[x][y] == 'X' else 0

    return result
    
#################################################################

input = get_input('day_3_input.csv')
print(add_claims(id_list))
print(count_conflicts())