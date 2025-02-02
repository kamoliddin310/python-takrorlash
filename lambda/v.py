from pprint import pprint

a = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
a.sort(key=lambda x: x['model'], reverse=True)
pprint(a)