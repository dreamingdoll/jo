def solution(classes, m):
    answer = 0
    for students in classes: # 교실별 학생 수 하나씩 대입
        answer += students // m # 교실별 학생 수 // 조교의 담당 인원 수   80 // 30  =>  2
        if students % m != 0: # 나머지가 있으면 조교의 담당 인원 수 + 1
            answer += 1
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
classes = [80, 45, 33, 20]
m = 30
ret = solution(classes, m)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")