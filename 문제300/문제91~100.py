
# 문제 91
inventory = {'메로나': [300, 20],
             '비비빅': [400, 3],
             '죠스바': [250, 100]}

# 문제 92
print(inventory.get('메로나')[0], "원")

# 문제 93
print(inventory.get('메로나')[1], "개")

# 문제 94
inventory.update({'월드콘': [500, 7]})
print(inventory)

# 문제 95
icecream = {'탱크보이': 1200,
            '폴라포': 1200,
            '빵빠레': 1800,
            '월드콘': 1500,
            '메로나': 1000}
icecream_list = list(icecream.keys())
print(icecream_list)

# 문제 96
icecream_list = list(icecream.values())
print(icecream_list)

# 문제 97
print(sum(icecream.values()))

# 문제 98
new_product = {'팥빙수': 2700, '아맛나': 1000}
icecream.update(new_product)
print(icecream)

# 문제 99
keys = ('apple', 'pear', 'peach')
vals = (300, 250, 400)
result = dict(zip(keys, vals))

print(result)

# 문제 100
date = ['09/05', '09/06', '09/08', '09/09']
close_price = [10500, 10600, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))

print(close_table)

