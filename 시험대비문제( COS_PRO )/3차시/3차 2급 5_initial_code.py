def solution(member_age, transportation):
	if transportation == 'Bus': # 이동수단이 버스면
		adult_expense = 40000 # 어른가격 = 40000원
		child_expense = 15000 # 아이가격 = 15000원
	elif transportation == 'Ship': # 이동 수단이 배면
		adult_expense = 30000 # 어른가격 = 30000원
		child_expense = 13000 # 아이가격 = 13000원

	elif transportation == 'Airplane': # 이동수단이 비행기면
		adult_expense = 70000 # 어른기격 = 70000원
		child_expense = 45000 # 아이가격 = 45000원

	if len(member_age) >= 10: # 일행 명수가 10명이 넘으면
		adult_expense *= 0.9 # 어른 가격의 90% 로 할인
		child_expense *= 0.8 # 아이 가격의 80% 로 할인

	total_expenses = 0 # 가격의 합계
	for age in member_age:
		if age >= 20: # 나이가 성인이면
			total_expenses += adult_expense # 가격합계에 어른 가격 저장
		else: # 나이가 아이이면
			total_expenses += child_expense # 가격합계에 아이 가격 저장

	return total_expenses # 가격의 합계 리턴


#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
member_age1 = [13, 33, 45, 11, 20]
transportation1 = "Bus"
ret1 = solution(member_age1, transportation1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

member_age2 = [25, 11, 27, 56, 7, 19, 52, 31, 77, 8]
transportation2 = "Ship"
ret2 = solution(member_age2, transportation2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")