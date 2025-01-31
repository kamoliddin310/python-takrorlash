from pprint import pprint
days = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31,
}
# A

# a = (input("Oy nomini kiriting --> "))
# if a in days:
#     print(f"{days[a]} kundan iborat.")
# else:
#     print("Bu nomli oy yuq")


# B

# a = days.items()
# v = sorted(a)
# pprint(v)


# C

# for i, v  in days.items():
#     if v == 31:
#         print(f"{i} {v}")


# D

# for day, count in sorted(days.items(), key=lambda x: (x[1], x[0])):
#     print(f"{count} {day}")


#  E

r = input("Oy nomini kiriting --> ")
if r in days:
    print(f"{days[r]} kundan iborat")
else:
    print("Bu oy mavjud emas")