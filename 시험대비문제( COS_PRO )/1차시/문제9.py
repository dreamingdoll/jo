

def solution(characters):
    result = ""
    result += characters
    # for i in range(len(characters)):
    for i in range(1, len(characters)):
        if characters[i-1] != characters[i]:
            result += characters[i]
    return result

characters = "senteeeencccccceeee"
ret = solution(characters)
print("solution 함수 결과", ret, ".")