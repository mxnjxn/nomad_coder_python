# adding arguments to the function

def say_hello(who="annaymous"):
    print("hello", who)


# can write anything in a required arguments unless it is a valid data type;
say_hello("Nicolas")
say_hello()


def plus(a, b):
    print(a + b)


def minus(a, b):
    print(a-b)

# giving a default value


def multiply(a, b=9):  # giving a default value of 9
    print(a * b)


plus(3, 5)

minus(34, 23)

multiply(3)

multiply(3, 4)
