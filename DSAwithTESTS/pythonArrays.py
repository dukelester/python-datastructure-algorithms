#introduction to python array
'''
Array is a collection of objects of same type stored in contiguous memory locations.
indexing starts from 0

Array can be in one dimension or multiple dimensions

 one dimension ==> one row and multiple  columns
 total memory = total number of elements * 4bytes
 
 multiple dimensions ==> multiple rows and multiple columns
 creating an array: import the array module 
 
 Complexity:
 space complexity ==> O(n)
 time complexity ==> O(1)
'''
from array import *
from os import RWF_NOWAIT
# array_name = array(type_code, [initialization])

marks = array('d', [34.678, 56.98, 67.099, 45,22,44])
marks_ = array('f', [34.678, 56.98, 67.099, 45,22,44])
marks__ = array('i', [2,4,6,8,0,5,3])
print(marks, marks_,marks__, sep="\n")


student_marks = array('i', [])

# numbers = eval(input("Enter the Number of subjects : \t"))
numbers = 5
for i in range(numbers):
    # mark = eval(input("Enter the marks of the subjects \t"))
    student_marks.append(i)
    
print(student_marks)


for m in student_marks:
    print(m , student_marks.index(m), sep=" index =>")
    print()
    
student_marks.reverse()
    
print(student_marks)
print(student_marks.buffer_info())

print(student_marks.count(20))
print(student_marks.tolist())
print(student_marks[3:], student_marks[-2], student_marks[1::])

#!using the numpy library

from numpy import *

my_data = array([
    [24, 4,3,5],
    [24, 4, 3, 5,],
    [ 8, 4, 5, 5],
    [1556,16,15,9]
    ])
print(my_data)
print(len(my_data))
data_2 = insert(my_data, i, [1,2,3,4], axis=1)
print(data_2)
data_3 = insert(data_2, 0, [3,4,5,6, 8], axis=0)
print()
print(data_3)
data_4 = append(data_2, [[90, 89, 78, 90, 70]], axis=0)
print('\n',data_4)

element_90 = data_4[4][0]
print(element_90)

for row in data_4: # O(m)
    # print(row)
    for col in row: # O(n)
        print(col)  # ==> O(m * n)
        
#search for an element in the 2 dimensional array

def searchIn2DArray(array, element):
    if len(array)  == 0:
        return array
    if len(array) == 1:
        return array[0][0]
    
    for row in range(len(array)):
        print('**********row index **********',row)
        for col in range(len(array[row])):
            if array[row][col] == element:
                
                return f'found at {(row, col)}'
            
print(searchIn2DArray(data_4,78))
print(data_4)
print()
data_5 = delete(data_4, 1, axis=0) #delete a row
data_5 = delete(data_4, 1, axis=1) #delete a column
print(data_5)

my_zipped = zip(data_4[0], data_4[2])
print(dict(my_zipped))

a = [1,2,3,4,5]
b = [4, 5, 6, 7, 8]

c = list(filter(lambda x: x in a, b))
print(len(c))
print(array_split(b, 8))