
# 문제 71
my_variable = ()

# 문제 72
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
print(type(movie_rank))

# 문제 73
t1 = (1,)
print(type(t1))

# 문제 74
# t = (1, 2, 3)
# t[0] = 'a'
"""
튜플의 요솟값은 한 번 정하면 지우거나 변경할 수 없다
"""

# 문제 75
# t = 1, 2, 3, 4
"""
tuple
"""

# 문제 76
t = ('a', 'b', 'c')
t = list(t)
t[0] = 'A'
t = tuple(t)
print(t)

# 문제 77
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)
print(type(interest), interest)

# 문제 78
interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest = tuple(interest)
print(type(interest), interest)

# 문제 79
"""
[예측]
apple banana cake
"""
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

# 문제 80
a = []
for i in range(99) :
    a.append(i + 1)

a = a[1::2]
a = tuple(a)
print(type(a), a)