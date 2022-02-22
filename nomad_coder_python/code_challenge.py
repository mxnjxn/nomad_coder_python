def plus(a, b):
    a = float(a)
    b = float(b)
    return a+b


def minus(a, b):
    a = float(a)
    b = float(b)
    return a-b


def multi(a, b):
    a = float(a)
    b = float(b)
    return a * b


def devide(a, b):
    a = float(a)
    b = float(b)
    return a/b


def remain(a, b):
    a = float(a)
    b = float(b)
    return a % b


def negative(a):
    a = float(a)
    return -a


def power(a, b):
    a = float(a)
    b = int(b)
    return a**b


# if plus functin includes "print", print(plus(2,3)) result in none
print(plus(2, 3))
# function include print; therefore, process print when activated.
plus_result = plus(3, "3")
print(plus_result)

minus_result = minus(3, "3")
print(minus_result)

multi_result = multi(4, "4")
print(multi_result)

devide_result = devide(4, "4")
print(devide_result)

remain_result = remain(5, "4")
print(remain_result)

negative_result = negative(5)
print(negative_result)

power_result = power(2, "3")
print(power_result)
