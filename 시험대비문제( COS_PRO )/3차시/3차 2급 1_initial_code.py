def func_a(scores, score):
    rank = 1 # 순위
    for s in scores: # 전체 점수를 하나씩 대입
        if s == score: # scores 리스트의 원소중 score(n번 학생의 점수)와 같은것을 찾으면
            return rank # 순위 리턴
        rank += 1 # 순위를 내리기
    return 0

def func_b(arr):
    arr.sort(reverse=True) # 리스트.sort(reverse=True) : 내림차순 정렬

def func_c(arr, n):
    return arr[n] # n번 학생이 해당하는 점수 리턴

def solution(scores, n):
    score = func_c(scores, n) # func_c 실행 : n번 학생이 해당하는 점수 구하기
    func_b(scores) # func_b 실행 : 리스트 내림차순 정렬
    answer = func_a(scores, score) # func_a 실행 : 순위 구하기
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores = [20, 60, 98, 59] # 학생들의 수험점수
n = 3
ret = solution(scores, n)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")


