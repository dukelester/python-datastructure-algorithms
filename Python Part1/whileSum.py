# Python program example to show the use of while loop  

num = 7000

count = 1
sum_ = 0
sum_squares = 0


while count <= num:
    sum_ += count
    if count % 2 ==0:
        sum_squares += count **2
    count += 1
print(sum_, sum_squares)


