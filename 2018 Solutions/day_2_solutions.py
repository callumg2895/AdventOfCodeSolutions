import csv

#################################################################
######################### Functions #############################

def get_input(input_file_name):
    with open(input_file_name, ) as input_file:
        return [str(row).strip('\r\n') for row in input_file]

def get_checksum(input):

        contains_letter_twice = 0
        contains_letter_thrice = 0

        for string in input:
                contains_letter_thrice += get_addition(string, 3)
                contains_letter_twice += get_addition(string, 2)

        return contains_letter_thrice * contains_letter_twice

def get_addition(string, x):

        letter_counts_dict = dict({})

        for letter in string:
                
                if letter in letter_counts_dict:                       
                        letter_counts_dict[letter] += 1
                else:
                        letter_counts_dict[letter] = 1   

        return 1 if (x in letter_counts_dict.values()) else 0

def find_common_letters(input):

        index = 0
        stop = False
        string1 = ''
        string2 = ''

        for string in input:
                for i in range(index):
                        if get_differences(string, input[i]) == 1:
                                stop = True
                                string1 = string
                                string2 = input[i]
                                break

                if stop:
                        break

                index += 1

        return get_similar_letters(string1, string2)
                
def get_differences(string1, string2):
        
        differences = 0
        index = 0

        while index < min(len(string1), len(string2)):
                differences += 1 if string1[index] != string2[index] else 0
                index += 1
        
        return differences

def get_similar_letters(string1, string2):

        print(string1)
        print(string2)
        similar_letters = ''
        index = 0

        while index < min(len(string1), len(string2)):

                if string1[index] == string2[index]:
                         similar_letters += string1[index]

                index += 1

        return similar_letters


#################################################################

input = get_input('day_2_input.csv')
print(get_checksum(input))
print(find_common_letters(input))

