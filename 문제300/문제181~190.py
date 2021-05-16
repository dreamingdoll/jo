
# 문제 181
first_floor = ["101호", "102호"]
second_floor = ["201호", "202호"]
third_floor = ["301호", "302호"]
apart = [first_floor, second_floor, third_floor]
print(apart)
# 문제 182
시가 = [100, 200, 300]
종가 = [80, 210, 330]
stock = [시가, 종가]

# 문제 183
시가 = [100, 200, 300]
종가 = [80, 210, 330]
stock = {"시가": 시가, "종가": 종가}

# 문제 184
stock = {"10/10" : [80, 110, 70, 90],
         "10/11" : [210, 230, 190, 200]}

# 문제 185
apart = [[101, 102], [201, 202], [301, 302]]
for i in range(3):
    for j in range(2):
        print(apart[i][j], "호")


# 문제 186
apart = [[101, 102], [201, 202], [301, 302]]
for i in range(3):
    for j in range(2):
        print(apart[2-i][j], "호")

# 문제 187
apart = [[101, 102], [201, 202], [301, 302]]
for i in range(3):
    for j in range(2):
        print(apart[2-i][1-j], "호")


# 문제 188
apart = [[101, 102], [201, 202], [301, 302]]
for i in range(3):
    for j in range(2):
        print(apart[i][j], "호", "\n-----")

# 문제 189
apart = [[101, 102], [201, 202], [301, 302]]
for i in range(3):
    if i > 0:
        print("-----")
    for j in range(2):
        print(apart[i][j], "호")

# 문제 190
apart = [[101, 102], [201, 202], [301, 302]]
for i in range(3):
    for j in range(2):
        print(apart[i][j], "호")
print("-----")