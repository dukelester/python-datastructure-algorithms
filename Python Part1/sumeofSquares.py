# Code to find the sum of squares of each element of the list using for loop  
  
# creating the list of numbers  
numbers = [3, 5, 23, 6, 5, 1, 2, 9, 8] 

sum_ = 0

for number in numbers:
    print(number **2)
    sum_ += number **2
    
print(sum_)


for num in range(0,len(numbers)):
    numbers.append(numbers[num] + 2)
    # numbers.remove(numbers[num])

print(numbers)

for num in range(len(numbers)):
    sum_ += numbers[num] ** 2

print(sum_)


import random
new_numbers = []
distinct = []
for num in range(0, 20):
    new_numbers.append(num)

    for i in range(len(new_numbers)):
        if num == new_numbers[i]:
            print(num)
            distinct.append(num)
print(new_numbers, distinct)

