

def solution(sentence):
    str = ''
    for c in sentence:
        if c != '.' and c != ' ': # 문자가 '.' 이 아니면서 공백이 아니면
        # if c != '.' and c != ' ':  문자가 '.' 이 아니거나 공백이 아니면
            str += c # str 에 문자 저장
    size = len(str)
    for i in range(size // 2):
        if str[i] != str[size - 1 - i]: # 첫 문자와 마지막 문자가 다르면 X
            return False
    return True

sentence1 = "never odd or even."
ret1 = solution(sentence1)
print("solution 함수 결과", ret1, ".")

sentence2 = "palindrome"
ret2 = solution(sentence2)
print("solution 함수 결과", ret2, ".")