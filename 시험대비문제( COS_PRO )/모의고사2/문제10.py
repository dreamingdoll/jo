def solution(time_table, n):
    answer = [0 for _ in range(n)]
    count = 0
    for i in range(len(time_table)):
        answer[count] += time_table[i]
        count  += 1
        if count >= n:
            count = 0
    return max(answer)
    # for i, j in enumerate(time_table):
    #     answer[i % n] += j
    #              [0 % 3] == 0
    #              [1 % 3] == 0
    #              [2 % 3] == 0
    #              [3 % 3] == 0
    #     a = max(answer)
    # return a




time_table = [1, 5, 1, 9]
n = 3
print(solution(time_table, n))

time_table = [4, 8, 2, 5, 4, 6, 7]
n = 4
print(solution(time_table, n))