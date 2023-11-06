import collections
"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

phone_time = collections.defaultdict(int)

max_time = 0
max_phone = ''

# Dictionary construction in O(n) - n being the number of telephone numbers
for records in calls:
    phone_time[records[0]] += int(records[3])
    phone_time[records[1]] += int(records[3])

# Runs in O(n) - n being number of telephone numbers
for phone, time in phone_time.items():
    if max_time < time:
        max_time = time
        max_phone = phone



print(f"{max_phone} spent the longest time, {max_time} seconds, on the phone during September 2016.")