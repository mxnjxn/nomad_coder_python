# Comparison between print() and return

#  always use return when the value of the function has to be initialized as other variable in further process.
def a_plus(a, b):
    print(a + b)


def plus(a, b):
    # returns kills the function. nothing is processed after the return line.
    return a+b


a_result = a_plus(2, 3)  # none

# 5 / when recalling functin using "return", function get replaced by the return value
result = plus(2, 3)

print(a_result, result)
