# 내 답
def solution(scores):
    grade_counter = [0 for i in range(5)]
    for x in scores:
        if x >= 85 and x <= 100: # 85점 ~ 100점
            grade_counter[0] += 1 # A + 1
        elif x >= 70 and x <= 84: # 70점 ~ 84점
            grade_counter[1] += 1 # B + 1
        elif x >= 55 and x <= 69: # 55점 ~ 69점
            grade_counter[2] += 1 # C + 1
        elif x >= 40 and x <= 54: # 40점 ~ 54점
            grade_counter[3] += 1 # D + 1
        else: # 0점 ~ 39점
            grade_counter[4] += 1 # F + 1
    return grade_counter

# 다른사람 답
#############################
"같음"
#############################
"같음"