
def solutions(purchase):
    total = 0
    for p in purchase:
        if p >= 1000000:
            total += 50000
        elif p >= 600000:
            total += 30000
        elif p >= 400000:
            total += 20000
        elif p >= 200000:
            total += 10000
    return total


purchase = [150000, 210000, 399990, 990000, 1000000]
ret = solutions(purchase)
print("solution 함수 결과", ret, ".")
