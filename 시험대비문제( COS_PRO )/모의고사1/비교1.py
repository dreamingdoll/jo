# 내 답
def func_a(k):
    sum = 0
    for i in range(k+1): # K+1 까지 반복
        sum += i # sum 에 1 더하기
    return sum # sum 리턴

def solution(n, m):
    sum_to_m = func_a(m)
    sum_to_n = func_a(n-1)
    answer = sum_to_m - sum_to_n
    return answer

# 다른사람 답
#############################
"같음"
#############################
"같음"
