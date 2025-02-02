o = int(input("yilni kiriting --> "))

s = lambda d: d % 4 == 0 or o % 400 == 0 and 100 != 0

print(s(o))

print("bu misolni flowgorithmda ishlagan edim")
