def solution(shirt_size):
    answer = [0 for _ in range(len(shirt_size))]
    for i in shirt_size:
        if i == "XS":
            answer[0] += 1
        elif i == "S":
            answer[1] += 1
        elif i == "XS":
            answer[2] += 1
        elif i == "L":
            answer[3] += 1
        elif i == "XL":
            answer[4] += 1
        elif i == "XXL":
                answer[5] += 1
    return answer

shirt_size = ["XS", "S", "L", "L", "XL", "S"]
print(solution(shirt_size))