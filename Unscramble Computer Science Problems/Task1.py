"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

set_of_num = set()

for text_records in texts:
    set_of_num.add(text_records[0])
    set_of_num.add(text_records[1])

for call_records in calls:
    set_of_num.add(call_records[0])
    set_of_num.add(call_records[1])

print(f"There are {len(set_of_num)} different telephone numbers in the records.")