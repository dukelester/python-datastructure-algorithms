"""
Arrays

"""

number_of_marks = eval(input("Enter the number of marks: "))
marksArray = []


for mark in range(0, number_of_marks):
    if mark % 2 == 0:
        marksArray.append(mark)


print(marksArray, end=" \n")

data = [567, 55,22,3,1,33,44,556,6,7,8,0, 'duke', 'lester']
data.sort()
data.sort(reverse=True)
print(data)