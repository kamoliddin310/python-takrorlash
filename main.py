class Student:
    davlati = "uzbekistan"
    shahar = "samarqand"

    def __init__(self, name, age, grade, phone):
        self.ismi = name
        self.yoshi = age
        self.sinfi = grade
        self.telefoni = phone
        


s1 = Student("ali", 16, 7, 43545435)

print(s1.davlati)
print(s1)

