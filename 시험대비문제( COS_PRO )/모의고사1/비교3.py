# 내 답
def func_a(arr, n):
    ret = []
    for x in arr:
        if x != n: # x가 n과 다르면
            ret.append(x) # ret 에 x 추가
    return ret

def func_b(a, b):
    if a >= b: # a 가 b보다 크거나 같으면
        return a - b # a - b 리턴
    else: # 아니면
        return b - a # b -  a 리턴

def func_c(arr):
    ret = -1
    for x in arr:
        if ret < x: # ret 이 x보다 작으면
            ret = x
    return ret

def solution(visitor):
    max_first = func_c(visitor)
    visitor_removed = func_a(visitor, max_first)
    max_second = func_c(visitor_removed)
    answer = func_b(max_first, max_second)
    return answer

# 다른사람 답
#############################
"같음"
#############################
"같음"