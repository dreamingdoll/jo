def func_a(current_grade, last_grade, rank, max_diff_grade):
    arr_length = len(current_grade) # 전체 학생수
    count = 0 # 장학생 수
    for i in range(arr_length): # 전체 학생수 만큼 반복
        if current_grade[i] >= 80 and rank[i] <= arr_length // 10: # 이번학기 성적이 80점 이상이면서 석차가 상위 10% 이내인 학생
            count += 1 # 장학생 + 1
        elif current_grade[i] >= 80 and rank[i] == 1: # 이번학기 성적이 80점 이상이면서 석차가 1등인 학생
            count += 1 # 장학생 + 1
        elif max_diff_grade > 0 and max_diff_grade == current_grade[i] - last_grade[i]: # 최대값이  양수이고 그 값이 (이번학기 성적 - 직전학기 성적 )의 값과 같으면
            count += 1 # 장학생 + 1
    return count # 장학생 수 리턴

def func_b(current_grade): # 각 학생별석차 구하기
    arr_length = len(current_grade) # len(리스트) : 리스트 내 요소들의 개수 구하기 / 전체 학생수
    rank = [1] * arr_length
    for i in range(arr_length): # 학생 수만큼 반복
        for j in range(arr_length): # 학생 수만큼 반복
            if current_grade[i] < current_grade[j]: # 이번학기[i] < 이번학기[j]
                rank[i] += 1 # 더 작으면 순위 내리기
    return rank


"""
i = 0   j = 0   j = 1   j = 2   j = 3   j = 4   j = 5
i가 1 증가할 떄마다 j는 5번씩 실행
"""

def func_c(current_grade, last_grade):
    max_diff_grade = 1 # 최대값 변수
    for i in range(len(current_grade)): # current_grade의 길이 만큼 반복
        max_diff_grade = max(max_diff_grade, current_grade[i] - last_grade[i]) # (이번학기 성적 - 직전학기 성적 )의 최대값 max_diff_grade 변수에 저장
    return max_diff_grade # (이번학기 성적 - 직전학기 성적 )의 최대값 리턴

def solution(current_grade, last_grade):
    rank = func_b(current_grade)  # func_b 함수의 결과를 rank 변수에 저장
    max_diff_grade = func_c(current_grade, last_grade) # func_c 함수의 결과를 max_diff_grade 변수에 저장
    answer = func_a(current_grade, last_grade, rank, max_diff_grade) # func_a 함수의 결과를 answer 변수에 저장
    return answer # answer 의 값 리턴

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
current_grade = [70, 100, 70, 80, 50, 95]
last_grade = [35, 65, 80, 50, 20, 60]
ret = solution(current_grade, last_grade)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")