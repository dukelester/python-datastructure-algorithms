import math
def countBits(number):
    number_of_bits = 0
    while number:
        number_of_bits += number & 1 #the bitwise operator
        number >>= 1
        print(number_of_bits)
    return number_of_bits

bits1 = countBits(10)
bits2 = countBits(20)

print(bits1, bits2)
import random
number = 456789.0987654567
print(math.isclose(number, 456789.098765))
print(random.randrange(50))
print(random.randint(40, 70))
print(random.random())
print(random.shuffle([number]))