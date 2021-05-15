#
# # 문제 121
# a = input("문자입력 : ")
# if a.islower() == True :
#     print(a.upper())
# elif a.islower() == False :
#     print(a.lower())
#
# # 문제 122
# score = int(input("점수 : "))
# if score >= 81 and score <= 100 :
#     print("grade is A")
# elif score >= 61 and score <= 80 :
#     print("grade is B")
# elif score >= 41 and score <= 60:
#     print("grade is C")
# elif score >= 21 and score <= 40:
#     print("grade is D")
# elif score >= 0 and score <= 20 :
#     print("grade is E")
#
# # 문제 123
# a = {"달러": 1167, "엔": 1.096, "유로": 1268, "위안": 171}
# b = input("알고싶은 환율 :")
# money, unit = b.split()
# print(int(money) * a[unit], "원")
#
#
# # 문제 124
# input_number1 = int(input("숫자1 : "))
# input_number2 = int(input("숫자2 : "))
# input_number3 = int(input("숫자3 : "))
#
# print(max(input_number1, input_number2, input_number3))
#
# # 문제 125
# a = {"011": "SKT", "016": "KT", "019": "LGU", "010": "None"}
# b = input("전화번호 : ")
# c = b.split("-")
# print(f"당신은 {a[c[0]]}사용자 입니다")
#
# # 문제 126
# a = {"010": "강북구", "011": "강북구", "012": "강북구",
#      "013": "도봉구", "014": "도봉구", "015": "도봉구",
#      "016": "노원구", "017": "노원구", "018": "노원구", "019": "노원구"}
#
# b = input("우편번호")
# print(a[b[:3]])
#
# # 문제 127
# a = {"1": "남자", "3": "남자",
#      "2": "여자", "4": "여자"}
# b = input("주민등록번호[형식 : 000000-0000000] : ")
# c = b.split("-")
# print(a[c[1][0]])
#
# # 문제 128
# b = input("주민등록번호[형식 : 000000-0000000] : ")
# c = b.split("-")
# d = c[1][1:3]
# print(d)
# if d <= "8" :
#     print("서울입니다")
# elif d >= "9" :
#     print("서울이 아닙니다")

# 문제 129
b = input("주민등록번호[형식 : 000000-0000000] : ")
c = b.split("-")
d = c[0] + c[1]
d = str(d)
e = 2
f = 0
a = 0
count = 1
while True:
    f += int(d[a]) * e
    a += 1
    e += 1
    count += 1
    if count == 8:
        e = 2
    if a == 9:
        break
d = str(d)
a = f % 11
if int(d[12]) == a:
    print("유효함")
else:
    print("유효하지않음")



# 문제 130

import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
if ( int(btc["opening_price"]) + ( int(btc["max_price"]) - int(btc["min_price"])) ) > int(btc["max_price"]):
    print("상승가")
if ( int(btc["opening_price"]) + ( int(btc["max_price"]) - int(btc["min_price"])) ) < int(btc["max_price"]):
    print("하락장")

