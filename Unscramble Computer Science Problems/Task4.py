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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

callers = set(call[0] for call in calls)
called = set(call[1] for call in calls)
texters = set(text[0]for text in texts)
texted = set(text[1] for text in texts)

telemarketers = set()

for caller in callers:
    if caller not in called and caller not in texters and caller not in texted:
        telemarketers.add(caller)

print("These numbers could be telemarketers: ")
for num in sorted(telemarketers):
    print(num)
