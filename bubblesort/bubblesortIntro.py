#create a bubble
# Bubble sort in Python

def bubbleSort(array):
    
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)

def BubbleSortMarks(marks):

    for mark in range(len(marks)):
        for m in range(0, len(marks) - mark - 1):

            if marks[m] > marks[m + 1]:
                temp_mark = marks[m]
                marks[m] = marks[m + 1]
                marks[m + 1] = temp_mark


marks = [23,78,9,46,3,33,67]
BubbleSortMarks(marks)

print('Sorted marks in Ascending Order:')
print(marks)