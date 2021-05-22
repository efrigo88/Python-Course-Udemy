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
    '1 - Buenos Aires - Argentina': 'America/Argentina/Buenos_Aires',
    '2 - Dubai': 'Asia/Dubai',
    '3 - Cuba': 'Cuba',
    '4 - Moscow - Russia': 'Europe/Moscow',
    '5 - Madrid - Spain': 'Europe/Madrid',
    '6 - Brussels - Europe': 'Europe/Brussels',
    '7 - Sydney - Australia': 'Australia/Sydney',
    '8 - Ulam Bator - Asia': 'Asia/Ulan_Bator' ,
    '9 - Tokio - Japan': 'Asia/Tokyo',
    '0 - Exit Program' : 'Exit'
    }

while True:
    
    print('Select one time zone from the list below: ')
    print()
    for time_zone in time_zones_dict:
        print(time_zone)

    print()
    selection = input('Choose a timezone from the menu: ')
    
    if selection == '0':
        print('You exited the time zone game')
        break

    if 0 < int(selection) < 10:
        for time_zone in time_zones_dict:
            if selection in time_zone:
                tz_to_display = pytz.timezone(time_zones_dict[time_zone])
                time_in_timezone = datetime.datetime.now(tz=tz_to_display)
                local_time = datetime.datetime.now()
                utc_time = datetime.datetime.utcnow()
                
                print('The time in {} is {}'.format(time_zones_dict[time_zone], time_in_timezone))
                print('The local time is {}'.format(local_time))
                print('The UTC time is {}'.format(utc_time))    
    else:
        print('Wrong number, try again')
    
    print()
    print('=' * 50)