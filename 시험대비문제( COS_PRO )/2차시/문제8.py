
def solutions(number):
    count = 0 # 자연수의 개수
    while number: # 정수가 있을때까지 반복
        n = number % 10 # 끝 한 자리 구하기
        if n == 2 or n == 3 or n == 5 or n == 7:
            # 끝 한자리가 2, 3, 5, 7 이면
            count += 1 # 자연수 개수 증가
        number //= 10 # 나머지 버리기
    return count

number = 290225331
ret = solutions(number)

print("solution 함수 결과", ret, ".")