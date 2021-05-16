
# 문제 161
for 변수 in range(0, 100):
    print(변수)


# 문제 162
for 변수 in range(2002, 2051, 4):
    print(변수)

# 문제 163
for 변수 in range(1, 31):
    if 변수 % 3 == 0:
        print(변수)

# 문제 164
for 변수 in range(0, 100, -1):
    print(변수)

# 문제 165
for 변수 in range(0, 10):
    print(float(변수/10))

# 문제 166
for 변수 in range(1, 10):
    print(f"3 x {변수} = {3*변수}")

# 문제 167
for 변수 in range(1, 10, 2):
    print(f"3 x {변수} = {3*변수}")

# 문제 168
더함 = 0
for 변수 in range(1, 11):
    더함 += 변수
print(더함)

# 문제 169
더함 = 0
for 변수 in range(1, 11, 2):
    더함 += 변수
print(더함)

# 문제 170
곱함 = 1
for 변수 in range(1, 11):
    곱함 *= 변수

print(곱함)
