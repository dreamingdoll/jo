def solution(cards):
    color = [0 for _ in range(3)]
    score = 0
    for card in cards:
        if card[0] == "red":
            color[0] += 1
        if card[0] == "black":
            color[1] += 1
        if card[0] == "blue":
            color[2] += 1
        score += int(card[1])
    if  3 in color:
        score *= 3
    if  2 in color:
        score *= 2
    return score

cards = [["blue", "2"], ["red", "5"], ["black", "3"]]
print(solution(cards))

cards = [["blue", "2"], ["blue", "5"], ["black", "3"]]
print(solution(cards))