a = [1, 2, 33, 5, 6, 7, 7]

d = int(input("Son kiriting --> "))

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == d:
            print(i,",",j)