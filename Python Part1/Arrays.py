from array import *

marks = array('i', [23,44,1,45,66,88])

print(marks)


for element in marks:
    print(element)

el = marks[0]
print(el)

#add an item
marks.insert(6, 800)


for element in marks:
    print(element)

marks[3] = 900
print(marks)

print(marks.index(900))

marks.remove(900)
print(marks)

#multidimensional array ==> 2d

temperatures = [
    [11, 12, 5, 2],[15, 6,10],[10, 8, 12, 5],[12, 15, 8, 6]
]

print(temperatures)
#the ist element 

element = temperatures[0][0]
print(element)

element_ = temperatures[3][0]
print(element_)

for t in temperatures:
    print(t)
    for k in t:
        print(k)

temperatures.insert(0, [900])
print(temperatures)

a = array('c',[['Mon',18,20,22,17],['Tue',11,18,21,18],
   ['Wed',15,21,20,19],['Thu',11,20,22,21],
   ['Fri',18,17,23,22],['Sat',12,22,20,18],
   ['Sun',13,15,19,16]])
m = reshape(a,(7,5))
print(m)