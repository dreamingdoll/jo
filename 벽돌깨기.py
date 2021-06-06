import pygame
import sys
from pygame.locals import *
import time
import random # 랜덤함수 불러오기

pygame.init()
화면 = pygame.display.set_mode((480, 640))
pygame.display.set_caption("벽돌깨기")
시간 = pygame.time.Clock()
pygame.key.set_repeat(1, 1)
배경 = pygame.image.load('배경.jpg')
점수 = 0
게임종료 = 0




def 벽돌그리기() :
    for 벽돌 in 벽돌리스트 :
        pygame.draw.rect(화면, ((random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255))), 벽돌)

def 공그리기() :
    pygame.draw.circle(화면, ((random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255))), (int(x), int(y)), 7)

x = int(480/2)
y = 640 - 10
dx = 10
dy = -10

패달세로 = 10
패달가로 = 100
패달x = (480 - 패달가로) / 2
패달 = pygame.Rect(패달x, 640-패달세로-10, 패달가로, 패달세로 )

벽돌리스트 = []
for 열 in range(6) :
    for 행 in range(10) :
        벽돌 = pygame.Rect(열*(60+10)+35, 행*(16+5)+34, 60, 15)

        벽돌리스트.append(벽돌)


def 패달그리기() :
    pygame.draw.rect(화면, ((random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255))), 패달)

while True :
    화면.blit(배경, (0, 0))
    if 게임종료 == 0 :
        x += dx
        y += dy

    if x + dx > 480 - 7 or x + dx < 7 :
        dx = -dx

    if y + dy < 7 :
        dy = -dy

    elif(y + dy > 630 ) :
        if x > 패달x and x < 패달x + 패달가로 :
            dy = -dy
        else :
            게임종료 = 1

    for 벽돌 in 벽돌리스트 :
        if x > 벽돌.x and x < 벽돌.x+벽돌.width and y > 벽돌.y and y < 벽돌.y+벽돌.height :
            dy = -dy
            벽돌리스트.remove(벽돌)
            점수 += 1

    for 동작 in pygame.event.get() :
        if 동작.type == QUIT :
            pygame.quit()

        elif 동작.type == pygame.KEYDOWN :
            if 동작.key == pygame.K_LEFT :
                패달.left -= 1
                패달x -= 1

            elif 동작.key == pygame.K_RIGHT :
                패달.right += 1
                패달x += 1

    글꼴1 = pygame.font.SysFont("malgungothic", 15)
    점수메세지 = 글꼴1.render("획득점수 :" +str(점수), True, ( (random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255)) ))
    화면.blit(점수메세지, (10, 10))

    if 게임종료 == 1:

        글꼴2 = pygame.font.SysFont("malgungothic", 30)
        종료메세지1 = 글꼴2.render("게임종료", True, ((random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255))))
        화면.blit(종료메세지1, (180, 300))

        글꼴3 = pygame.font.SysFont("malgungothic", 20)
        종료메세지2 = 글꼴3.render("획득점수 : " + str(점수), True, ((random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255))))
        화면.blit(종료메세지2, (185, 350))

    벽돌그리기()
    공그리기()
    패달그리기()

    pygame.display.update()
    시간.tick(30)