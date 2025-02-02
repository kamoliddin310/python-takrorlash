# import json
# from pprint import pprint

# f = open("products.json")
# json_str = f.read()

# json_lst: list[dict] = json.loads(json_str)

# # pprint(max(json_lst, key=lambda i: i["narx"]))
# # pprint(min(json_lst, key=lambda i: i["narx"]))

# # pprint(sorted(json_lst, key=lambda i: i["narx"]))
# # print("\n")
# # pprint(sorted(json_lst, key=lambda i: i["narx"], reverse=True))

# name = input("Qidirayotgan narsangizning nomini kiriting --> ")

# pprint(filter(lambda i: name.lower() in i["nomi"], json_lst))


# with open("products.json") as f:

#     json_str = f.read()

#     product_list: list[dict] = json.loads(json_str)

#     new_product = {
#         "nomi": input("nomi >> "),
#         "narx": int(input("narxi >> ")),
#         "turi": input("turi >> ")
#     }
#     product_list.append(new_product)

# with open("products.json", "w") as f:

#     json_str = json.dumps(product_list, indent=4)

#     f.write(json_str)