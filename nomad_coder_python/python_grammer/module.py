# module is a set of functions that user can import in a program
# you don't want to import all the function set in module math. Rather imoport specific module.
from return_me import plus  # able to import python file in your computer.
import math

from math import ceil, fsum
from math import fsum as sexy_sum  # able to change name of the function

print(math.ceil(1.2))
print(math.fabs(1.2))
print(math.fabs(-1.2))  # absolute number

print(ceil(1.2))
print(fsum([1, 2, 3, 4, 5, 6]))

print(sexy_sum([1, 2, 3, 4, 5, 6, 7]))

print(plus(2, 3))
