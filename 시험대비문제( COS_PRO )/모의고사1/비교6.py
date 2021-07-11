# 내 답
def solution(height, k):
    answer = 0
    n = len(height) # n의 길이
    for h in height:
        if h > k:
            answer += 1
    return answer

# 다른사람 답
#############################
def solution(height, k):
    answer = 0
    n = len(height)
    for h in height:
        if h >= k+1:
            answer += 1
    return answer
#############################
def solution(height, k):
    answer = 0
    n = len(height)
    for h in height:
        if h-1 >= k:
            answer += 1
    return answer
