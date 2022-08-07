
import random

def linear_search(marks, target):
    if len(marks) == 0:
        return None
    for i in range(0, len(marks)):
        # print(marks[i])

        if marks[i] == target:
            return i

    else: 
        return None

marks = [89, 67, 34, 20, 78, 90, 3, 69]
target = 900

marks_ = []

result = linear_search(marks, target) #call function
print(result)

result_ = linear_search(marks_, target) #call function
print(result_)
    
random_marks = []
for k in range(2, 2000):
    random_marks.append(k)

print(random_marks)

target_mark = 199
answer = linear_search(random_marks, target_mark)
print(answer)

#O(n)