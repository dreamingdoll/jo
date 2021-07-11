
def solution(attack, recovery, hp):
    count = 0
    print(f"현재 몬스터의 hp : {hp}\n--------------------")
    while(True):
        count += 1
        print(f"공격합니다! \n데미지 {attack}")
        hp -= attack
        if hp <= 0:
            print(f"hp : 0\n")
            break
        print(f"hp : {hp}\n")
        print(f"몬스터가 회복 마법을 사용합니다! \n{recovery} 회복")
        hp += recovery
        print(f"hp : {hp}\n")
    return count

attack = 30
recovery = 10
hp = 60

ret = solution(attack, recovery, hp)
print("총 공격 횟수 :", ret, "회")
