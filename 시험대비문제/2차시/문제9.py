

def solutions( votes, N, K):
    counter = [0 for _ in range(N + 1)]

    for x in votes :
        counter[x] += 1
    answer = 0
    for c in counter:
        if c == K :
            answer += 1
    return answer

votes = [2, 5, 3, 4, 1, 5, 1, 5, 5, 3] # 투표 결과
N = 5 # 투표자 수
K = 2 # 받은 투표수 찾는 변수
ret = solutions(votes, N, K)

print("solution 함수 결과", ret, ".")