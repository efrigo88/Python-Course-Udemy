# Write a small program to display information on the
# four clocks whose functions we have just looked at:
# i.e. time(), perf_counter, monotonic() and process_time().
#
# Use the documentation for the get_clock_info() function
# to work out how to call it for each of the clocks.

import time

clock_name = 'time'
clock_info= time.get_clock_info(clock_name)
print(f'Information about time(): {clock_info}')

print()

clock_name = 'perf_counter'
clock_info= time.get_clock_info(clock_name)
print(f'Information about perf_counter(): {clock_info}')

print()

clock_name = 'monotonic'
clock_info= time.get_clock_info(clock_name)
print(f'Information about monotonic(): {clock_info}')

print()

clock_name = 'process_time'
clock_info= time.get_clock_info(clock_name)
print(f'Information about process_time(): {clock_info}')

