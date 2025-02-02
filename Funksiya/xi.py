find_root = lambda n: next((x for x in range(n + 1) if x * x == n), -1)

n = int(input("N sonini kiriting: "))

result = find_root(n)
print(result)
