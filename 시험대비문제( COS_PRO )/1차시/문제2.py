# 문제 2
def solution (price, grade):
    answer = 0
    if grade == "V":
        answer = price - price*0.15
    if grade == "G":
        answer = price - price*0.1
    if grade == "S":
        answer = price - price*0.05


    return int(answer)

price1 = 2500
grade1 = "V"
ret1 = solution(price1, grade1)

print("solution : return value of the function is", ret1, ".")

price2 = 96900
grade2 = "S"
ret2 = solution(price2, grade2)

print("solution : return value of the function is", ret2, ".")