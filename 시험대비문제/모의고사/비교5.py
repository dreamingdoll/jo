# 내 답
def solution(stones):
    cnt = 0
    current = 0
    n = len(stones)
    while n > current:
        current += stones[current]

        cnt += 1
    return cnt

# 다른사람 답
#############################
"같음"
#############################
"같음"