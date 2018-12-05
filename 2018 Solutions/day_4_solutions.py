import csv
import time
import datetime as dt

#################################################################
######################### Variables #############################

t_last = 0

timestamps = []
current_guard = ['']

events = dict({})
datetimes = dict({})
guards = dict({})
guards_list = []

#################################################################
######################### Functions #############################

def get_input(input_file_name):
    with open(input_file_name, newline = '') as input_file:
        for row in input_file:

            item = str(row).strip('\r\n')

            t_raw =  dt.datetime.strptime(item[1:17], '%Y-%m-%d %H:%M')
            t_stamp = get_total_minutes(t_raw)

            timestamps.append(t_stamp)
            
            datetimes[t_stamp] = t_raw

            
            events[t_stamp] = get_id(item[26:len(item)]) if item[19] == 'G' else item[19]


def get_id(string):

    numbers = '0123456789'
    result = ''

    for i in string:
        if i in numbers:
            result += i

    return result


def get_total_minutes(obj):
    return (int(obj.year) * 365 * 24 * 60) + (int(obj.month) * 31 * 24 * 60) + (int(obj.day) * 24 * 60) + (int(obj.hour) * 60) + int(obj.minute)


def iterate_timestamps():
    while True:
        
        current_timestamp = min(timestamps)

        timestamps.remove(current_timestamp)

        if len(timestamps) > 0:

            next_timestamp = min(timestamps)
            handle_event(current_timestamp, next_timestamp)
            
        else:
            break

        
def handle_event(current_t, next_t):
    event = events[current_t]
    current_date = datetimes[current_t]
    next_date = datetimes[next_t]

    if event == 'f':
        sleep_guard(current_date, next_date)
    elif event == 'w':
        pass
    else:
        change_guard(event)


def sleep_guard(current_date, next_date):
    for i in range(current_date.minute, next_date.minute):
        guards[current_guard[0]][i] += 1


def change_guard(guard):
        current_guard[0] = guard

        if guard not in guards_list:
            guards_list.append(guard)
            guards[guard] = [0 for i in range(60)]


def analyse_guards():

    sleepiest_guard = ''
    current_longest_time_slept = 0
    guard_sleepiest_mins = dict({})
    guard_time_asleep = dict({})

    for guard in guards_list:

        current_sleepiest_minute = 0
        time_asleep = 0
        current_guard_shift = guards[guard]

        for minute in range(60):
            time_slept = current_guard_shift[minute]
            time_asleep += time_slept

            if time_slept > current_guard_shift[current_sleepiest_minute]:
                current_sleepiest_minute = minute

        guard_sleepiest_mins[guard] = current_sleepiest_minute
        guard_time_asleep[guard] = time_asleep

        if time_asleep > current_longest_time_slept:
            current_longest_time_slept = time_asleep
            sleepiest_guard = guard

    print(int(sleepiest_guard) * guard_sleepiest_mins[sleepiest_guard])

    max_time_spent_asleep_on_sleepiest_minute = 0
    current_sleepiest_minute = 0
    sleepiest_guard = ''

    for guard in guards_list:

         time_spent = guards[guard][guard_sleepiest_mins[guard]]

         if time_spent > max_time_spent_asleep_on_sleepiest_minute:
             max_time_spent_asleep_on_sleepiest_minute = time_spent
             sleepiest_guard = guard
    
    print(int(sleepiest_guard) * guard_sleepiest_mins[sleepiest_guard])
 
#################################################################

get_input('day_4_input.csv')
iterate_timestamps()
print(analyse_guards())