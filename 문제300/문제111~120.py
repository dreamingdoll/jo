
# 문제 111
a = input("입력 : ")
print(a)

# 문제 112
b = int(input("입력 : "))
print(b + 10)

# 문제 113
c = int(input("입력 : "))
if c > 0 and c % 2 == 0:
    print("짝수")

elif c == 0:
    print("홀수도, 짝수도 아니다")

else:
    print("홀수")

# 문제 114
d = int(input("입력 : "))
if d + 20 > 255:
    print(255)
else:
    print(d + 20)

# 문제 115
e = int(input("입력 : "))
if e - 20 > 255:
    print(255)

elif e - 20 < 0:
    print(0)

else:
    print(e - 20)

# 문제 116
f = input("현재 시간입력, 형식 => [00:00] : ")
if f[3:] == "00":
    print("정각입니다")

if f[3:] != "00":
    print("정각이 아닙니다")

# 문제 117
fruit = ["사과", "포도", "홍시"]
g = input("좋아하는 과일은? : ")
if g in fruit:
    print("정답입니다")
else:
    print("오답입니다")

# 문제 118
warn_investment_list = ["Microsoft", "Gppgle", "Naver", "Kakao", "SAMSUNG", "LG"]

g = input("투자종목 : ")
if g in warn_investment_list:
    print("투자 경고 종목입니다")
else:
    print("투자 경고 종목이 아닙니다")

# 문제 119
fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

g = input("좋아하는 계절은? : ")
if g in fruit.keys():
    print("정답입니다")
else:
    print("오답입니다")

# 문제 120
fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

g = input("좋아하는 과일은? : ")
if g in fruit.values():
    print("정답입니다")
else:
    print("오답입니다")

