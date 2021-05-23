# 문제 4

def func_a(arr):
    counter = [0 for _ in range(1001)] # 각 자연수의 개수 세기
    for x in arr: # 리스트 반복
        counter[x] += 1 #
    return counter # 각 자연수 인덱스에 +1

def func_b(arr): # 가장 많이 등장하는 수 세기
    ret = 0 # 가장 많은 개수를 가지고 있는 자연수를 찾아서 저장하는 변수
    for x in arr:
        if ret < x: # 현재 자연수보다 해당 자연수가 더 많으면
            ret = x # 해당 자연수가 가장 큰 자연수가 됨
    return ret

def func_c(arr): # 가장 적게 등장하는 수 세기
    INF = 1001
    ret = INF
    for x in arr:
        if x != 0 and ret > x: # 0이 아닐시 가장 작은수보다 작으면
            ret = x # 해당 자연수가 가장 작은 자연수가 됨
    return ret

def solution(arr):
    counter = func_a(arr)
    max_cnt = func_b(counter)
    min_cnt = func_c(counter)
    return max_cnt // min_cnt

arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]
ret = solution(arr)

print("solution : return value of the function is", ret, ".")