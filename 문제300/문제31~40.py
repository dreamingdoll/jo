
# 문제 31
"""
[예상]
34
"""

# 문제 32
"""
[예상]
HiHiHi
"""

# 문제 33
print('-' * 80)

# 문제 34
t1 = 'python '
t2 = 'java '
print((t1 + " " + t2 + " ") * 4)

# 문제 35
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: % s 나이: %d " % (name1, age1))
print("이름: % s 나이: %d " % (name2, age2))



# 문제 36
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: {} 나이: {} " .format(name1, age1))
print("이름: {} 나이: {} " .format(name2, age2))

# 문제 37
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

# 문제 38
상장주식수 = "5,969,782,550"
상장주식수 = int(상장주식수.replace(",", ""))
print(상장주식수, type(상장주식수))

# 문제 39
분기 = "2020/03(E) (IFRS연결)"
분기 = 분기[:7]
print(분기)

# 문제 40
data = "    삼성전자    "
data = data.strip()
print(data)
