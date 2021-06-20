def solution(ladders, win):
    answer = 0
    player = [1, 2, 3, 4, 5, 6]
    for e in ladders: # 가로 사다리[  플레이어 위치 교환 ]
        # 교환 [ swap ] : 2개의 변수를 교환하는 방법
        temp = player[e[0]-1] # 첫번쨰 사다리를 temp 에 저장
        player[e[0]-1] = player[e[1]-1] # 두번째 사다리를 첫번째 사다리에 저장
        player[e[1]-1] = temp # temp 를 두번쨰 사다리에 저장
    answer = player[win-1]
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
ladders = [[1, 2], [3, 4], [2, 3], [4, 5], [5, 6]]
win = 3
ret = solution(ladders, win)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")