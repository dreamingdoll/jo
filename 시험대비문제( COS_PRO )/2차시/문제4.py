import math

def solution(words):
    answer = ''
    for i in words:
        if len(i) >= 5:
            answer += i
    if answer == '':
        return "empty"
    return answer

word1 = ["my", "favorite", "color", 'is', "violet"]
ret1 = solution(word1)
print("solution 함수 결과", ret1, ".")

word2 = ["yes", "I", "am"]
ret2 = solution(word2)
print("solution 함수 결과", ret2, ".")