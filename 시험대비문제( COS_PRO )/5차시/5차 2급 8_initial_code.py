def solution(usage):
    answer = 0
    if usage > 30: # 상수도가 30 초과하면
        answer = 20 * 430 + 10 * 570 + (usage - 30) * 840
        # 20톤 가격, 10톤 가격 + 30톤을 뺀 * 840
        # 1단계 + 2단계 + 3단계
    elif usage > 20: # 그 외 상수도가 20 이하이면
        answer = 20 * 430 + (usage - 30) * 570 # 1단계, 2단계
    else:
        answer = usage * 430 # 1단계
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니 위의 코드만 수정하세요.
usage = 35
ret = solution(usage)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")