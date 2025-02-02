o = input()

s = lambda a: ''.join(filter(lambda c: c.isdigit(), a))
print(s(o))