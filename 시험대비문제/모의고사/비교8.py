# 내 답
def solution(name_list):
    answer = 0
    for name in name_list:
        for n in name:
            if n == 'j' or n == 'k':
                answer += 1
                break
    return answer

# 다른사람 답
#############################
"같음"
#############################
"같음"