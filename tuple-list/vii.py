a = list(input("raqam kiriting --> "))

c = 0
for i in a:
    if a.count(i) == 1:
        c += 1
        print(i)
print("\n",c,"ta bor")