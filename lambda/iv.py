a = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("input: ", a)
s = sorted(a, key=lambda x: x[1])

print("output", s)