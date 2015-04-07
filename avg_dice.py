#!/usr/bin/env python
from random import randint

rolls = []
for i in range(0, 100000):
	rolls.append(randint(1,6))

print float(sum(rolls)/len(rolls))
