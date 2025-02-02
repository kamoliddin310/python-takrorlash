a = [123, 456, 789, 852, 12, 42, 61, 369]

print(list(filter(lambda x: str(x)[0] in "2468", a)))