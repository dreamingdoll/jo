def solution(price, grade):
    answer = 0
    if grade == "S":
        answer = price*0.95
    if grade == "G":
        answer = price*0.9
    if grade == "V":
        answer = price*0.85
    return int(answer)


price1 = 2500
grade1 = "V"
print(solution(price1, grade1))

price2= 96900
grade2 = "S"
print(solution(price2, grade2))