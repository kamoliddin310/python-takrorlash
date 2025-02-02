from pprint import pprint
a = [
    {"Name": "Asil", "age": 9, "cars": 3},
    {"Name": "Laziz", "age": 19, "cars": 2},
    {"Name": "Sardor", "age": 25, "cars": 7},
    {"Name": "Og`abek", "age": 5, "cars": 5},
]

pprint(list(filter(lambda x : x["age"] > 18 and x["cars"] > 1, a)))