# 내 답
def solution(stones):
    cnt = 0
    current = 0
    n = len(stones) # n = stones 의 길이
    while n > current: # n 이 stones 보다 클 때 까지 반복
        current += stones[current] # current + (stones current 번째 인덱스)
        cnt += 1 # cnt + 1
    return cnt

# 다른사람 답
#############################
"같음"
#############################
"같음"