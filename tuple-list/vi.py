a = [123, 456, 789, 852, 12, 42, 61, 369]

print(list(filter(lambda i: str(i)[0] in '02468', a)))