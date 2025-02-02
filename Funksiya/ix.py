a = int(input("faqat juft sonlar kiriting --> "))

if len(str(a)) % 2 == 0:  

    b = list(map(int, str(a)))

    r = list(map(lambda x, y: x + y, b[::2], b[1::2]))
    f = ",".join(map(str, r))
    print(f)
else:
    print("sonlar juft emas :( ")