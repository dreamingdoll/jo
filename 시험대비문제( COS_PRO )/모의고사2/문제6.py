def solution(words, word):
    answer = 0
    for i in words:
        for x, y in zip(i, word):
            if x != y:
                answer += 1

    return answer

words = ["CODE", "COED", "CDEO"]
word = "CODE"
print(solution(words, word))

"""
zip(word1, word2)
(word1-1, word2-1)
(word1-2, word2-2)
(word1-3, word2-3)

"""