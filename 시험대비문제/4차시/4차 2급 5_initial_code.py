def solution(calorie):
    # min_cal = calorie[0] # 정답 : 모든 열량보다 큰 수의 임의의 값
    min_cal = 1000
    answer = 0
    for cal in calorie: # 모든열량을 하나씩 cal 대입
        if cal > min_cal: # 현재 열량이 최소 열량보다 크면
            answer += cal - min_cal  # 현재 열량 - 최소 열량
        min_cal = min(min_cal, cal) # 최소 열량과 현재 열량 중 작은 값을 최소 열량값으로 저장
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
calorie = [713, 665, 873, 500, 751]
ret = solution(calorie)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")