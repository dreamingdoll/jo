"""
print
정의 : 입력한 코들르 출력할 때 사용
사용방법 : print(입력)

type()
정의 : 입력한 것의 class가 무엇인지 확인
사용방법 : type()입력
int()
정의 :입력한 것을 정수로 변환
사용방법 : int(입력)
str()
정의 : 입력한 것을 문자로 변환
사용방법 :str(입력) :
float()
정의 : 입력한 것을 실수로 변경
사용방법 :float(입력)

인덱싱
정의 :특정 장소에 데이터를 저장하는 것

슬라이싱
정의 : 원하는 부분의 문자를 가져오는 것
사용방법 : 문자[시작값: 끝값: 간격]

replace()
정의 : 문자의 특정 부분을 원하는 것으로 바꾸는 것
사용방법 : 문자변수.replace("바꿀값", "바꾸고싶은 값")

split()
정의 : 문자열을 공백 혹은 어떠한 기준으로 나눌때 사용하는 함수
사용방법 : 변수.split()

formatting 이란
formatting : % => %s : 문자 형식, %d : 정수 형식

format()
정의 : 문자열 중간 중간에 특정 변수의 값을 넣어주기 위해서 사용하는 함수
사용방법 : print("- {} - {} " .format(변수1, 변수2))

f-string
사용방법 : print(f"- {변수1} - {변수2}")

strip()
정의 : 공백제거함수
사용방법 : 변수.strip()

upper()
정의 : 대문자변환함수
사용방법 : 변수.upper()

lower()
정의 : 소문자변환함수
사용방법 : 변수.lower()

endswith()
정의 : 끝나는 문자가 맞는지 확인하는 함수
사용방법 : 변수.endswith("문자")

startswith()
정의 : 정의 : 시작하는 문자가 맞는지 확인하는 함수
사용방법 : 변수.startswith("문자")

rsplit()
정의 : 오른쪽 공백제거함수
사용방법 : 변수.rstrip()

리스트와 변수 차이
변수 : 저장공간 => 변수이름 = 변수
리스트 : 여러대의 변수를 저장하는 공간 => 리스트이름 = [변수1, 변수2, 변수3, 변수4, .....]

append()
정의 : 리스트 변수 추가함수
사용방법 : 리스트이름.append(추가할변수)

insert()
정의 : 해당 인덱스 위치에 변수를 삼입
사용방법 : 리스트이름.insert(인덱스번호, 추가할변수)

del
정의 : 해당 인덱스 위치에 변수를 제거
사용방법 : del 리스트명[인덱스번호]

remove()
정의 : 리스트 변수 제거함수
사용방법 : 리스트이름.remove(제거할변수)

max()
정의 : 리스트 안 변수중 최대값
사용방법 : max(리스트명)

min()
정의 : 리스트 안 변수중 최소값
사용방법 : min(리스트명)

sum()
정의 : 리스트 안 변수 더하기
사용방법 : sum(리스트명)

len()
정의 : 리스트의 길이 구하기
사용방법 : len(리스트명)

join함수
정의 :
사용방법 :

\n
정의 : 줄바꿈함수

\t
정의 : Tap

리스트 오름차순
list.sort()

리스트 내림차순
list.sort(reverse = True)



# 데이터를 저장하는 방법 4가지의 차이와 사용방법
    변수 : 1개 저장 상자 / 수정 가능
    사용방법 : 변수명 =

    리스트 : 여러개를 저장할 수 있는 저장 상자 / 수정 가능
    사용방법 : 리스트명 = []

    튜플 : 리스트처럼 여러 개의 데이터를 담아두는 저장 상자 / 수정 불가
    사용방법 : 튜플명 = ('a', 'b')

    딕셔너리 :  key(키)와 value(값)을 한 쌍으로 데이터를 저장하는 저장 상자 / 수정 가능
    사용방법 : 딕셔너리명 = {}



튜플을 리스트로
list(튜플명)

리스트를 튜플로
tuple(리스트명)

튜플 언팩킹
정의 : 튜플의 각 요소를 여러 개의 변수에 할당하는 것
사용방법 : 변수1, 변수2, 변수3 = 튜플명

딕셔너리활용
딕셔너리 리스트 추가 : 딕셔너리명[키값] = []
딕셔너리 키만 출력 : 딕셔너리명.keys()
딕셔너리 값만 출력 : 딕셔너리명.values()
두개의 딕셔너리 합치기 : 딕셔너리명1.update(딕셔너리명2)
2개의 튜플 딕셔너리 변환 : 딕셔너리명 = dict(zip(튜플1, 튜플2))
키 [리스트 ], 값 [라스트] 딕셔너리 변환 : 딕셔너리명 = dict(zip(키 [리스트 ], 값 [라스트]))

논리 : 맞는지 틀린지 판단
연산자 :
    산술연산자 : + 더하기, - 빼기, * 곱하기, ** 제곱, / 나누기, // 몫, % 나머지
    비교연산자 : > 초과, < 미만,  >= 이상, <= 이하, == 같다, != 같지않다
    논리연산자 : and 이면서, or 이거나, ! 부정
    대입연산자 : = 오른쪽 값을 왼쪽에 대입
               += 오른쪽 값을 왼쪽값에 더한 후 왼쪽에대입
               -= 오른쪽 값을 왼쪽값에 뺀 후 왼쪽에대입
               *=, /=, %= 등

if 활용
정의 : 조건을 판단하여 해당 조건에 맞는 코드를 실행하는 데 사용
샤용방법:
    if 논리 :
        참[ 코드 ]
    elif 논리2 :
        참[ 코드2 ]
    elif 논리3 :
        참[ 코드3 ]
    elif 논리4 :
        참[ 코드4 ]
    else :
        거짓[ 코드 ]


if 변수 in 리스트명 :
정의 : 만약 변수가 해당 리스트에 있다면

input()
정의 : 사용자가 입력한 값을 변수에 저장하는 함수
활용
변수 = input("...")

반복문 = 기준에 따른 반복

1. for 변수명 in list명 : 리스트 내 모든 변수를 하나 씩 변수명에 대입
2. for 벼누 in range(시작값, 끝값 전까지, 증감 단위) : 시작 값부터 끝값까지 증감하면서 변수명에 하나 씩 대입
        - range(값) : 값 만큼 반복 실행
        - range(시작값, 끝값) : 시작 값부터 끝값 전 까지 1씩 증가하면서 반복
        - range(시작값, 끝값 전까지, 증감 단위) : 시작 값부터 끝값까지 증감하면서 변수명에 하나 씩 대입

배수 구하기
방법 : 배수 % 숫자
예) 3의 배수 구하기
if 숫자 % 3 == 0:
    print("True")

홀수/짝수 판별
숫자 % 2 == 0 => 짝수
숫자 % 2 != 0 => 홀수
"""


"""
    # 2 ~ 9단 구구단 만들기
for 단 in range(2, 10) : # 2 부터 9까지 1씩 증가하며 단에 하나씩 대입
    for 곱 in range(1, 10) : # 1부터 9까지 1씩 증가하며 곱에 하나씩 대입
        print(단, "x", 곱, "=", (단*곱))

# 단은 8번 반복 / 곱은 단이 1씩 증가할 때마다 9번씩 반복 = 72번 반복

    # * 피라미드 만들기
for 변수 in range(1, 6) :
    print(" "*(6-변수), "*"*(2*변수-1))
"""
"""

알고리즘 = 순서도 = 코드 명령 순서
      *       1줄    =   공백 4개           별 1개    현재 줄 수 * 2  2-1
     ***      2줄    =   공백 3개           별 2개    현재 줄 수 * 2  4-1
    *****     3줄    =   공백 2개           별 3개    현재 줄 수 * 2  6-1
   *******    4줄    =   공백 1개           별 4개    현재 줄 수 * 2  8-1
  *********   5줄    =   공백 0개           별 5개    현재 줄 수 * 2  10-1
            1씩 증가     1씩 감소           2개씩 증가
            
         range(1, 6)   " "*(6-현재줄수)      "*"*(2*현재줄수-1)

"""



