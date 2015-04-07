def list_flip(list):
	temp = []
	for n in xrange(1, len(list)+1):
		temp.append(list[len(list)-n])
	flip = temp
	return flip

a = [1, 2, 3, 4]
b = ['a', 'b', 'c', 'd']

a_flip = list_flip(a)
b_flip = list_flip(b)

print a, a_flip
print b, b_flip