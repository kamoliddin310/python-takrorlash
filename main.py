import json


with open("products.json") as f:

    json_str = f.read()

    product_list: list[dict] = json.loads(json_str)

    new_product = {
        "nomi": input("nomi >> "),
        "narx": int(input("narxi >> ")),
        "turi": input("turi >> ")
    }
    product_list.append(new_product)

with open("products.json", "w") as f:

    json_str = json.dumps(product_list, indent=4)

    f.write(json_str)
