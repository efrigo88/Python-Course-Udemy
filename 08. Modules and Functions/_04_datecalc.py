# import time

# print(time.gmtime(0))
# print(time.localtime())
# print(time.time())

# time_here = time.localtime()
# print(type(time_here))

# print()
# print(time_here)
# print(f'Year: {time_here[0]} or {time_here.tm_year}')
# print(f'Month: {time_here[1]} or {time_here.tm_mon}')
# print(f'Day: {time_here[2]} or {time_here.tm_mday}')

# The time game
import time
# from time import time as my_timer
# from time import monotonic as my_timer
from time import perf_counter as my_timer
import random

input('Press enter to start')

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()

input('Press enter to stop')

end_time = my_timer()

print('Started at ' + time.strftime('%X', time.localtime(start_time)))
print('Ended at ' + time.strftime('%X', time.localtime(end_time)))

print(f'Your reaction time was {end_time - start_time} seconds')

