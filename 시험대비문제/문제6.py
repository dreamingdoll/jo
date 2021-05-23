def solution(number):
             count = 0
             for i in range(1, number + 1):
                 current = i # 현재 숫자
                 temp = count # 임시 변수에 박수 횟수 저장
                 while current != 0:
                     if current % 10 == 3 or current % 10 == 6 or current % 10 == 9:
                         # 현재숫자 / 10 했을때 나머지가 3, 6, 9 이면
                         count += 1 # 박수 숫자 올리기
                         print("pair", end='')
                     current = current // 10 # 현재 숫자 // 10 자릿수 내리기
                 if temp == count:
                     print(i, end= '')
                 print(" ", end= '')
             print("")
             return count

number = 40
ret = solution(number)

print("solution : return value of the function is", ret, ".")