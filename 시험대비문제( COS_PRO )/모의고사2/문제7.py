def solution(지역):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    위험지역 = 0
    for 가로 in range(4):
        for 세로 in range(4):
            check = True
            for height in range(4):
                if 0 <= 가로+dx[height] and 가로+dx[height] < 4 and 0 <= 세로 +dy[height] and 세로+dy[height] < 4:
                    if 지역[ 가로+dx[height] ][ 세로+dy[height] ] <= 지역[가로][세로]:
                        check = False
            if check:
                위험지역 += 1
    return 위험지역




지역 = [[3, 6, 2, 8], [7, 3, 4, 2], [8, 6, 7, 3], [5, 3, 2, 9]]
print(solution(지역))