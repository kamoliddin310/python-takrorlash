a = [1,2,3,4,5,6,7,8,9,10]

toq = []
for i in a:
    if i % 2 != 0:
        toq.append(i)

juft = []
for i in range(len(a), 1, -1):
    if i % 2 == 0:
        juft.append(i)

if len(toq) != len(juft):
    print("Toq va juft sonlar soni teng emas!")
else:
    c = []
    for i in range(len(toq)):
        c.append(toq[i])
        c.append(juft[i])

print(c)
