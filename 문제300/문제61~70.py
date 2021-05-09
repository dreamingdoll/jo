
# 문제 61
price = ['20180728', 100, 130, 140, 150, 160, 170]
price = price[1:]
print(price)

# 문제 62
nums = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10]
print(nums[::2])

# 문제 63
nums = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10]
print(nums[1::2])

# 문제 64
nums = [1 ,2 ,3, 4, 5]
print(nums[::-1])

# 문제 65
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

# 문제 66
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(' '.join(interest))

# 문제 67
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print('/'.join(interest))

# 문제 68
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print('\n'.join(interest))

# 문제 69
string = "삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest)

# 문제 70
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)
