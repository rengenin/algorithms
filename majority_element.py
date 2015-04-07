#!/usr/bin/env python
import random

items = [1, 2, 3, 4, 5, 5, 5, 5, 5 ]
# shuffle the items
random.shuffle(items)

print("shuffled items:", items)

majority_elem = items[0]
count = 1
for i in range(1,len(items)):
    if items[i] == majority_elem:
        count += 1
    else: 
        count -= 1
        if count == 0:
            majority_elem = items[i]
            count = 1

print("majority element : %d" % majority_elem)
