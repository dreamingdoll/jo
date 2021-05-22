
# 문제 191
print("##############")
data = [[2000, 3050, 2050, 1980],
        [7500, 2050, 2050, 1980],
        [15450, 15050, 15550, 14900]]

for i in data:
    for j in i:
        print(j * 1.00014)

# 문제 192
print("##############")
for i in data:
    print("----")
    for j in i:
        print(j * 1.00014)

# 문제 193
print("##############")
result = []
for i in data:
    for j in i:
        result.append(j * 1.00014)
print(result)

# 문제 194
print("##############")
result_in = []
for i in data:
    result = []
    result_in.append(result)
    for j in i:
        result.append(j * 1.00014)
print(result_in)

# 문제 195
print("##############")
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for i in ohlc[1:]:
    print(i[3])

# 문제 196
print("##############")
for i in ohlc[1:]:
    if i[3] > 150:
     print(i[3])

# 문제 197
print("##############")
for i in ohlc[1:]:
    if i[3] >= i[0]:
     print(i[3])

# 문제 198
print("##############")
volatility = []
for i in ohlc[1:]:
    volatility.append(i[1] - i[2])
print(volatility)

# 문제 199
print("##############")
for i in ohlc[1:]:
    if i[3] > i[0]:
     print(i[1] - i[2])

# 문제 200
n = 0
print("##############")
for i in ohlc[1:]:
    n += 1
    print(f"{n}일차 수익 {i[3] - i[0]}원")
