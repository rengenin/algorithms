from itertools import groupby

a = ['192.168.0.1','10.10.2.5', '10.3.6.7', '192.168.0.1', '10.10.2.5', '192.168.0.1']

print a

a = sorted(a)

print a

b = [len(list(group)) for key, group in groupby(a)]

print b