def binarySearch(data, target):
    first_element = 0 # position of the first element
    last_element = len(data) -1  #index / position/location of the last element

    while first_element <= last_element:
        midpoint = len(data) // 2 # to get the middle position in data
        midpoint = ( first_element + last_element) // 2

        if data[midpoint] == target:
            return midpoint
        
        elif data[midpoint] < target:
            first_element =  midpoint + 1

        elif data[midpoint] > target:
            last_element = midpoint - 1
            
    return None


data = [89, 67, 34, 20, 78, 90, 3, 69]
target = 90

result = binarySearch(data, target)
print(result)

random_marks = []
for k in range(2, 2000):
    random_marks.append(k)

print(random_marks)

target_mark = 194
answer = binarySearch(random_marks, target_mark)
print(answer)

# def check(data, target):
 
#     first_element = 0
#     mid = len(data) // 2

#     print(f'the mid position is {mid}')

#     if data[mid] == target:
#         return mid
#     else:
#         print("does not lie in the middle")
#         return "not found in the middle"
# marks = [67, 8, 90, 55, 30]  
# result = check(marks, 55)
# print(result)
