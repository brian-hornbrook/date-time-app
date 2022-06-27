import datetime as datetime

current_time = datetime.datetime.now()

# date formatted in numbers
date_numeric = current_time.strftime('%m/%d/%y')
print("Today's Date: " + date_numeric)

# date formatted in words
date_write = current_time.strftime('%B %d, %Y')
print("Today's Date: " + date_write)

# date and time formatted
date_time = current_time.strftime('%B %d, %Y %I:%M %p')
print("Today's Date and Time: " + date_time)
