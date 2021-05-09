
# 1. 게임에 필요한 라이브러리[파일]을 import
import random
import sys

import pygame # 파이게임 파일 불러오기
from pygame.locals import QUIT, Rect, KEYDOWN, K_UP, K_LEFT, K_RIGHT, K_DOWN, K_SPACE
#                        종료/ 그리기/ 키눌렀을떄/ 위키/ 왼쪽키/ 오른쪽키/ 아래키

# 2. 게임에 필요힌 기본 설정
pygame.init() # 파이게임 초기값
화면 = pygame.display.set_mode((1000, 1000)) # 화면 구성
프레임 = pygame.time.Clock() # 프레임에 파이게임 시간 설정
# Frame Per Second : FPS : 초당 프레임[정지사진] 수


음식 = [] # 여러개의 음식을 저장할 리스트
뱀 = [] # 여러개의 뱀 꼬리 저장할 리스트
(가로, 세로) = (50, 50) # 가로길이 세로길이 # 튜플선언


# 배경 넣기
배경 = pygame.image.load("뱀게임배경이미지.jpg")

# 배경음악 넣기
pygame.mixer.music.load("뱀게임배경음악.mp3")
pygame.mixer.music.play(-1)


# 3. 함수 만들기
    # 1. 음식 생성 함수 : 뱀이 음식을 먹었을 때 새로운 음식 추가 혹은 게임 시작시 음식 추가

def 음식생성() :
    while True:
        위치 = ( random.randint(0, 가로-1), random.randint(0, 세로-1))
               # 0 ~ 49 의 난수 생성
        if 위치 in 음식 or 위치 in 뱀 : # 해당 위치에 음식이나 뱀이 있으면
            continue # while 다시 실행

        else: # 해당 위치에 음식이나 뱀이 없으면
            음식.append(위치)
            break


# 2. 음식 이동 함수

def 음식이동(위치) :
    임의변수 = 음식.index(위치) # 해당 위치의 음식 찾기
    del 음식[임의변수] # 해당 위치에 음식 삭제
    음식생성() # 음식생성 함수 호출[새로운 음식 생성]

# 3. 그리기 함수
게임종료메세지 = None
def 그리기(점수판, 게임종료메세지) :
    화면.fill((0, 0, 0)) # 검정색으로 칠하기
    화면.blit(배경, (0, 0))

    # 음식 그리기
    for food in 음식:
        pygame.draw.ellipse(화면, (0, 255, 0), Rect(food[0] * 20, food[1] * 20, 20, 20))

    # 뱀 그리기
    for body in 뱀[::2]:
        pygame.draw.rect(화면, (0, 0, 0), Rect(body[0] * 20, body[1] * 20, 20, 20))
    for body in 뱀[1::2]:
        pygame.draw.rect(화면, (255, 255, 255), Rect(body[0] * 20, body[1] * 20, 20, 20))

    # 점수 그리기
    if 점수판 != None : # 점수에 내용이 있으면
        화면.blit(점수판, (10, 10))

    # 종료 메세지 그리기
    if 게임종료메세지 != None:
        화면.blit(게임종료메세지, (280, 500))


    pygame.display.update() # 화면 업데이트



# 4. 게임실행

my글꼴 = pygame.font.SysFont("hy헤드라인m", 30) # 글꼴, 글짜 크기
my글꼴2 = pygame.font.SysFont("hy헤드라인m", 40)
키 = K_DOWN
게임종료 = False # 게임종료 스위치
점수 = 0
뱀.append( (int(세로/2), int(가로/2)) ) # 뱀을 가운데에 배치


for i in range(30): # 30개의 음식 생성
    음식생성()

while True: # 계속 반복하기
    # 키보드 동작하기
    for 동작 in pygame.event.get(): # 파이게임 이벤트[동작]이 있을경우
        if 동작.type == QUIT : # 동작 이벤트가 종료하면
            pygame.quit() # 파이게임 종료
            sys.exit() # 시스템[모든코드] 종료
        elif 동작.type == KEYDOWN : # 키를 눌렀을 떄
            키 = 동작.key

    # 키를 눌렀을 때
    if not 게임종료 : # 게임종료가 False 이면
        if 키 == K_LEFT:
            머리 = (뱀[0][0] - 1, 뱀[0][1])
        elif 키 == K_RIGHT:
            머리 = (뱀[0][0] + 1, 뱀[0][1])
        elif 키 == K_UP:
            머리 = (뱀[0][0], 뱀[0][1] - 1)
        elif 키 == K_DOWN:
            머리 = (뱀[0][0], 뱀[0][1] + 1)

        # 뱀 몸에 닿았을 때 혹은 화면 밖으로 나갔을 때 게임종료
        if 머리 in 뱀 or 머리[0] < 0 or 머리[0] >= 세로 or 머리[1] < 0 or 머리[1] >= 가로  :
            게임종료메세지 = my글꼴2.render("게임종료 [ 최종점수 : " + str(점수) + " ]", True, (255, 255, 255))
            그리기(점수판, 게임종료메세지)
            게임종료 = True

        # 뱀 머리 추가
        뱀.insert(0, 머리)
        if 머리 in 음식 : # 만약 머리가 음식에 닿았을 때
            음식이동(머리) # 새로운 음식 추가
            점수 += 1 # 음식을 먹을때마다 1점 추가

        else: # 음식을 못먹으면
            뱀.pop() # 리스트내 가장 뒤에있는 항목 제거


        점수판 = my글꼴.render("전체 먹은 횟수 : " + str(점수), True, (255, 255, 255))
        속도 = 점수 // 10




    그리기(점수판, 게임종료메세지)
    프레임.tick(5 + 5*속도)

