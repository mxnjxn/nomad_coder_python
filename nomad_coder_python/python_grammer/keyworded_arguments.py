# a, b is a positional arguments as it depends on the positioin.
def a_plus(a, b):
    return a + b


result = a_plus(2, 4)
print(result)

# ****Preferred*** keyworded arguments/ position does not matter
result1 = a_plus(b=30, a=1)
print(result1)


def say_hello(name, age):
    return "Hello name you are age years old"


hello = say_hello(age="12", name="nico")
print(hello)


#
def say_hello(name, age):
    return "Hello name you are age years old"


hello = say_hello("nico", "12")
print(hello)

# in order to put variable in the string, input "f" in front of the string and then put {} around the string you would like to convert it into variable.


def say_hello(name, age):
    return f"Hello {name} you are {age} years old"


# the order that you write it crucial;therefore, the keyworded argument type is recommended
hello = say_hello("nico", "12")
print(hello)

# or


def say_hello(name, age):
    return "Hello " + name + " you are " + age + " years old"


hello = say_hello("nico", "12")
print(hello)
