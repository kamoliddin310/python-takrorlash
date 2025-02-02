a = [4,1,2,1,2]

c = len(list(filter(lambda x: a.count(x) == 1, a)))
s = list(filter(lambda x: a.count(x) == 1, a))

print(c, " --> ", s)