a = list(input("xoxlaganizcha son kirirting -- >"))
print(a)
c = 0
for i in a:
    if a.count(i) == 1:
        c += 1
        print(i)
print(c)