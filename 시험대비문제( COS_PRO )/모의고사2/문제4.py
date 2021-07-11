def solution(words):
    answer = ''
    for i in words:
        if len(i) >= 5:
            answer += i
    if answer == "":
        return "empty"
    return answer

words1= ["my", "favorite", "color", "is", "violet"]
print(solution(words1))

words2 = ["yes", "I", "am"]
print(solution(words2))