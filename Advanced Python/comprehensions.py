data = [ x ** x for x in range(0, 30) if (x ** x ) %2 ==0]
print(data)
even = [ d % 2 == 0 for d in data]
print(even)

# [ expression for loop if condition ]

even_numbers = [x for x in range(0, 100) if x % 2 ==0 ]
print(len(even_numbers))

names = ['Steve','Bill','Ram','Mohan','Abdul']

names_with_a = [name for name in names if 'a' in name]
print(names_with_a)

squares = [x**2 for x in range(0, 11)]
print(squares)

nums1 = [8, 3 ,4, 5,7]
nums2 = [6, 4, 5, 7, 8]

points = [(x, y) for x in nums1 for y in nums2]
print(points)

both_5_and_2 = [ number for number in range(200) if number %2 == 0 if number %5 == 0]
print(both_5_and_2)

#flatten a mattrix
mattrix = [
    [23,3,4,5,6],[8,4,0,6,8,20,9], [90,3,4,6,8,3],[67,2,3]
]

flattened = [ number for row in mattrix for number in row ]
print(flattened)