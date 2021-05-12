import time

print('The epoch on this systen starts at {}'.format(time.strftime('%c', time.gmtime(0))))

print(f'The current timezone is {time.tzname[0]} with an offset of {time.timezone}')

if time.daylight != 0:
    print('\tDaylight saving time is in effect for this location')
    print(f'\tThe DST timezone is {time.tzname[1]}')

print('Local time is {}'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
print('UTC time is {}'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())))