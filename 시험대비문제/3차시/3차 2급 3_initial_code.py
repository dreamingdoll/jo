#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(scores):
    #여기에 코드를 작성해주세요.
    answer = 0
    scores.remove(max(scores)) # scores 리스트에서 가장 큰 원소 삭제
    scores.remove(min(scores)) # scores 리스트에서 가장 작은 원소 삭제
    answer += int(sum(scores) / len(scores)) # 평균 = (scores 리스트 원소들의 합) 나누기 (리스트의 길이)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores1 = [35, 28, 98, 34, 20, 50, 85, 74, 71, 7]
ret1 = solution(scores1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

scores2 = [1, 1, 1, 1, 1]
ret2 = solution(scores2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")