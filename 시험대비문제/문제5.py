# 문제 5
def solution(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        # 첫번째값[좌] 첫번째값[우] = 첫번째값[우] 첫번째값[좌]
        left += 1 # 왼쪽 + 1
        right -= 1 # 오른쪽 + 1
    return arr


"""
left 0 일경우 right 0 => 반복문 실행
    arr[0], arr[0] = arr[0], arr[0]
    1       1        1       1
    left + 1   right - 1
left 0 일경우 right -1
    arr[1], arr[1] = arr[1], arr[1]
    4       3        3       4
    left + 1   right - 1

"""
arr = [1, 4, 2, 3]
ret = solution(arr)

print("solution : return value of the function is", ret, ".")