# 내 답
def solution(s):
    s_lst = list(s)
    n = len(s)
    for i in range(n):
        if s_lst[i] == 'a':
            s_lst[i] = 'z'
        elif s_lst[i] == 'z':
            s_lst[i] =  'a'
    return "".join(s_lst)

# 다른사람 답
#############################
def solution(s):
    s_lst = list(s)
    n = len(s)
    for i in range(n):
        if s_lst[i] == 'a':
            s_lst[i] = 'z'
        if s[i] == 'z':
            s_lst[i] =  'a'
    return "".join(s_lst)
#############################
def solution(s):
    s_lst = list(s)
    n = len(s)
    for i in range(n):
        if s_lst[i] == 'a':
            s_lst[i] = 'z'; continue
        if s_lst[i] == 'z':
            s_lst[i] =  'a'
    return "".join(s_lst)
