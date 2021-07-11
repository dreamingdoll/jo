import math

def solution(N, M):
    answer = 0
    if N < M:
        for i in range(N, M + 1):
            if i % 2 == 0:
                answer += i ** 2
    return answer

N = 4
M = 7
ret = solution(N, M)
print("solution 함수 결과", ret, ".")