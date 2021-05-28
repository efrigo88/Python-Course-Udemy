# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

import datetime
import pytz

time_zones_dict = {
    '1': 'America/Argentina/Buenos_Aires',
    '2': 'Asia/Dubai',
    '3': 'Cuba',
    '4': 'Europe/Moscow',
    '5': 'Europe/Madrid',
    '6': 'Europe/Brussels',
    '7': 'Australia/Sydney',
    '8': 'Asia/Ulan_Bator',
    '9': 'Asia/Tokyo',
    '0': 'Exit the Program'
    }

while True:
    
    print('Select one time zone from the list below: ')
    print()
    for time_zone in time_zones_dict:
        print('{}. {}'.format(time_zone, time_zones_dict[time_zone]))

    print()
    selection = input('Choose a timezone from the menu: ')
    
    # controling an empty input
    if not selection:
        print('Please do not provide an empty answer')
    
    # controling letters
    elif selection.isalpha():
        print('Please choose numbers between 0 and 9')
    
    elif selection == '0':
        print('You exited the time zone game')
        break
    
    elif selection in '123456789':
        for time_zone in time_zones_dict:
            if selection in time_zone:
                tz_to_display = pytz.timezone(time_zones_dict[time_zone])
                time_in_timezone = datetime.datetime.now(tz=tz_to_display)
                local_time = datetime.datetime.now()
                utc_time = datetime.datetime.utcnow()
                
                print('The time in {} is {}'.format(time_zones_dict[time_zone], time_in_timezone.replace(tzinfo=None, second=0, microsecond=0)))
                print('The local time is {}'.format(local_time.replace(second=0, microsecond=0)))
                print('The UTC time is {}'.format(utc_time.replace(second=0, microsecond=0)))
                
    else:
        print('Wrong number, try again')
    
    print()
    print('=' * 50)