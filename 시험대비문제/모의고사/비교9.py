# 내 답
def solution(price, money):
    answer = 0
    answer = money - sum(price)
    if answer < 0:
        return -1
    else:
        return answer

# 다른사람 답
#############################
def solution(price, money):
    answer = 0
    if sum(price) > money:
        answer = -1
    else :
        answer = money - sum(price)
    return answer
#############################
def solution(price, money):
    answer = 0
    sum=0
    for i in price:
        sum += i
    if money<sum :
        return -1
    else :
        answer = money - sum
        return answer
