# 내 답
def solution(arr, k):
    answer = 0
    ret = []
    for i in arr:
        for j in i:
            ret.append(j)
    ret.sort()
    answer = ret[k-1]
    return answer

# 다른사람 답
#############################
def solution(arr, k):
    return sorted([n for seq in arr for n in seq])[k - 1]
#############################
def solution(arr, k):
    ans_arr = []
    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            ans_arr.append(arr[i][j])
    ans_arr = sorted(ans_arr)
    return ans_arr[k-1]
