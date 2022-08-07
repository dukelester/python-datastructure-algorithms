# #a program to display prime numbers between 100 and 200

# for number in range(1, 10):
#     if number > 1:
#         for i in range(2, number):
#             if number % i == 0:
#                 # print(number)
#                 break
#             else:
#                 print(number)
    
    



#range is 100 to 200

# for number in range(100, 201):
#     # print(number)
  
#     for num in range(101, number):
#         if number % num == 0:
#             break
#         else:
#             print(number)


for num in range(100, 201):
    if all(num % i !=0 for i in range(2, num)):
        print(num)
        
for number in range(300, 701):
    if all(number % i !=0 for i in range(2, number)):
        print(number)
        
import random
# sorting a list
myNumbers =[]
for num in range (20, 500):
    myNumbers.append(num)
    
myNumbers.sort()
print(myNumbers)


#sort manually


        
