def solution(people):
    answer = [0 for _ in range(4)]
    for i in people:
        if i < 95:
            answer[0] += 1
        if i < 100 and i >= 95:
            answer[1] += 1
        if i < 105 and i >= 100:
            answer[2] += 1
        if i >= 105:
            answer[3] += 1
    return answer

people = [97, 102, 93, 100, 107]
print(solution(people))