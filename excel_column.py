#!/usr/bin/env python

class Solution:
    # @return a string
    def convertToTitle(self, num):
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        print capitals
        result = []
        while num > 0:
            result.append(capitals[(num-1)%26])
            num = (num-1) // 26
        result.reverse()
        return ''.join(result)

test = Solution().convertToTitle(220)
print test