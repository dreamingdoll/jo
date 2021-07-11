def soluion(scores):
    answer = 0
    scores.remove(max(scores))
    scores.remove(min(scores))
    answer = sum(scores) // len(scores)
    # answer = (sum(scores) - max(scores) - min(scores)) // (len(scores) - 2)
    return answer

scores1 = [35, 28, 98, 34, 20, 50, 80, 74, 71, 7]
print(soluion(scores1))

scores2 = [1, 1, 1, 1, 1]
print(soluion(scores2))