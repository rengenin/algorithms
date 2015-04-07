#!/usr/bin/env python

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
    	
    	majorityElement = num[0]
    	count = 1
    	
    	for i in xrange(1, len(num)):
    		if num[i] == majorityElement:
    			count += 1
    		else:
    			count -= 1
    			if count == 0:
    				majorityElement = num[i]
    				count = 1

    	return majorityElement 