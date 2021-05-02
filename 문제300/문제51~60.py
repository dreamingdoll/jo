
# 문제 51
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)

# 문제 52
movie_rank.append("배트맨")
print(movie_rank)

# 문제 53
movie_rank = ["닥터 스트레인지", "스플릿", "럭키", "배트맨"]
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

# 문제 54
movie_rank = ["닥터 스트레인지", "슈퍼맨", "스플릿", "럭키", "배트맨"]
movie_rank.remove("럭키")
print(movie_rank)

# 문제 55
movie_rank = ["닥터 스트레인지-", "슈퍼맨", "스플릿", "배트맨"]
del movie_rank[2]
del movie_rank[2]
print(movie_rank)

# 문제 56
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

# 문제 57
nums = [1, 2, 3, 4, 5, 6, 7]
nums_max = max(nums)
nums_min = min(nums)
print(f"max: {nums_max}\nmin: {nums_min}")

# 문제 58
nums = [1, 2, 3, 4, 5]
nums_sum = sum(nums)
print(nums_sum)

# 문제 59
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
cook_len = len(cook)
print(cook_len)

# 문제 60
nums = [1, 2, 3, 4, 5]
nums_sum = sum(nums)
nums_len = len(nums)
average = nums_sum / nums_len
print(average)


