# 문제 1
def solution(shirt_size):
    size_count = [0, 0, 0, 0, 0, 0] # 티셔츠 사이즈별 개수를 담을 리스트 선언

    for ss in shirt_size :
        if ss == "XS":
            size_count[0] += 1
        if ss == "S":
            size_count[1] += 1
        if ss == "M":
            size_count[2] += 1
        if ss == "L":
            size_count[3] += 1
        if ss == "XL":
            size_count[4] += 1
        if ss == "XXL":
            size_count[5] += 1
    return size_count

shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size)
print("solution : return value of the function is", ret, ".")

