def solution(N, M):
    answer = 0
    for i in range(N, M+1):
        if i % 2 == 0:
            answer += i**2
    return answer

N = 4
M = 7
print(solution(N, M))