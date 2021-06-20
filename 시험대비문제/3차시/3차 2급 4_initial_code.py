#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(words, word):
    #여기에 코드를 작성해주세요.
    count = 0 # 오타수
    for i in words:# words 리스트의 길이만큼 반복
        for j in range(len(i)): # i(words 리스트의 원소) 의 길이만큼 반복
            if i[j] != word[j]: #  i(words 리스트의 원소) 의 j번째 글짜가 word 의 j번째 글짜와 같으면
                count += 1 # count + 1

    # for comp in words:
    #     for x, y in zip(comp, word): # 검사단어 = x, 찾는단어 = y
    #         if x != y : # 검사 단어와 찾는 단어가 같지 않으면
    #             count += 1 # 오타 증가



    return count

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
words = ["CODE", "COED", "CDEO"]
word = "CODE"
ret = solution(words, word)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")