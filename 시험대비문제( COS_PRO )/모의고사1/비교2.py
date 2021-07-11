# 내 답
def func_a(s): # 최고 점수
    ret = 0
    for i in s: # s에서 i 가져오기
        if i > ret: # i 가 ret 보다 크면
            ret = i
    return ret

def func_b(s): # 모든 과목 점수의 합
    ret = 0
    for i in s: # s에서 i 가져오기
        ret += i # ret 에 i 더하기
    return ret

def func_c(s): # 최저 점수
    ret = 101
    for i in s: # s에서 i 가져오기
        if i < ret: # i 가 ret 보다 작으면
            ret = i
    return ret


def solution(scores):
    sum = func_b(scores) # 모든 과목 점수의 합
    max_score = func_a(scores) # 최고 점수
    min_score = func_c(scores) # 최저 점수
    return sum - max_score - min_score # (모든 과목 점수의 합) - (최고 점수) - (최저 점수)의 값을 return

# 다른사람 답
#############################
"같음"
#############################
"같음"