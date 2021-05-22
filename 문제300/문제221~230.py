
# 문제 221
def print_reverse(a):
    print(a[::-1])
print_reverse("asd")

# 문제 222
def print_score(a):
    print(sum(a)/len(a))
print_score([1, 2, 3])

# 문제 223
def print_even(a):
    for i in a:
        if i % 2 == 0:
            print(i)

print_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 문제 224
def print_keys(a):
    print(a.keys())
print_keys({"이름":"김말똥", "나이":30, "성별":0})

# 문제 225
mt_dict = {"10/26": [100, 130, 100, 100],
           "10/27": [10, 12, 10, 11]}
def print_value_by_key(a, b):
    print(a.get(b))

# 문제 226
def print_5xn(a):
    b = 0
    for i in range(len(a)+1):
        if i % 5 == 0 and i != 0:
            print(a[b:i])
            b = i
        else:
            print(a[b:])

print_5xn("아이엠어보이유알어걸")

# 문제 227
def print_mxn(a, c):
    b = 0
    for i in range(len(a)+1):
        if i % c == 0 and i != 0:
            print(a[b:i])
            b = i
        else:
            print(a[b:])
print_mxn("아이엠어보이유알어걸",3)

# 문제 228


# 문제 229


# 문제 230

