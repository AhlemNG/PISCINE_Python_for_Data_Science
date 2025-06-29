
import time
import datetime


#current time in seconds since the epoch
current_time = time.time()

print(f"Seconds since January 1, 1970: {current_time:.4f}2 or {current_time:.2e} in scientific notation")

#current date 

current_date = datetime.datetime.now()

print(current_date.strftime("%b %d %y"))