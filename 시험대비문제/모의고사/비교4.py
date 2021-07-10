# 내 답
def solution(scores):
    grade_counter = [0 for i in range(5)]
    for x in scores:
        if x >= 85 and x <= 100:
            grade_counter[0] += 1
        elif x >= 70 and x <= 84:
            grade_counter[1] += 1
        elif x >= 55 and x <= 69:
            grade_counter[2] += 1
        elif x >= 40 and x <= 54:
            grade_counter[3] += 1
        else:
            grade_counter[4] += 1
    return grade_counter

# 다른사람 답
#############################
"같음"
#############################
"같음"