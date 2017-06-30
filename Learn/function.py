def add1(a, b):
    if a > b:
        c = a + b
    else:
        c = a - b
    return print(c)


add1(5, 4)


def power(a):
    return a * a


print(power(5))


# 请计算a2 + b2 + c2 + ……。
def ce(*number):
    sum1 = 0
    for n in number:
        sum1 = sum1 + n * n
    return sum1

print(ce(1, 2, 3, 4))
