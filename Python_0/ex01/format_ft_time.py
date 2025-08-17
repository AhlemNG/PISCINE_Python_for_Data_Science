import time as t
import datetime as dt

current_time = t.time()
print(
    f"Seconds since January 1, 1970: {current_time:.4f} or "
    f"{current_time:.2e} in scientific notation")
current_date = dt.datetime.now()
print(current_date.strftime("%b %d %y"))
