#module is a python file
from calc import sum
import calc

import calc as thecalc

from calc import sum, average, power
from calc import *

import sys

print(calc.sum(34, 80))
print(sum(90, 4))

print(type(calc))

print(thecalc.sum(80, 45))

print(power(3, 9), average(30, 90))

print(sys.path)

print(calc.__doc__, calc.__file__, calc.__name__, calc.__package__)
# print(calc.__dict__)

