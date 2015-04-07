#!/usr/bin/env python

def cyclicCheck(head):

	slowTrace = head
	fastTrace = head

	while fastTrace != None and fastTrace.next != None:
		slowTrace = slowTrace.next
		fastTrace = fastTrace.next.next

		if (fastTrace == slowTrace):
			print "This is a circular list"
			return False

	print "This is a non - circular list"
	return True

class Element:
	def __init__(self,data,next=None):
		self.data = data
		self.next = next

if __name__ == "__main__":
	import doctest
	doctest.testmod()