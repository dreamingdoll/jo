# 문제 3
def func_a(month, day):
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    for i in range(month - 1): # 월 - 1 만큼 반복
        total += month_list[i] # 입력한 월의 전 월 까지의 일수를 다 더하기
    total += day # 내가 입력한 월의 일수 더하가
        # 총 1월 1일부터  내가 입력한 날짜 까지의 일수를 구하기
    return total - 1

def solution(start_month, start_day, end_month, end_day):
    start_total = func_a(start_month, start_day) # 시작 날짜
    end_total = func_a(end_month, end_day) # 끝날짜
    return end_total - start_total# 끝날짜 - 시작날짜

start_month = 1 # 시작 날짜의 월
start_day = 2 # 끝나는 날짜의 일
end_month = 2 # 끝나는 날짜의 월
end_day = 2 # 끝나는 날짜의 일
ret = solution(start_month, start_day, end_month, end_day)

print("solution : return value of the function is", ret, ".")