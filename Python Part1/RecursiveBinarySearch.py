import sys

print(sys.getrecursionlimit())
# sys.setrecursionlimit(20)

def hello(name):
    print(f'Greetings to you {name}')
    return hello(name)

# hello("duke")   

def findArea(length, width):
    area = length * width
    print(f'area is {area}')

    return findArea(length, width)

# findArea(90, 50)



def recursiveBinarySearch(data, target):
    if len(data) == 0:
        return None

    else:
        midpoint = len(data) //2 #find the mid point position
        if data[midpoint] == target:
            print(f' found at the middle {midpoint}')
            return True

        elif data[midpoint] < target:
            new_half = data[midpoint + 1 :]
            return recursiveBinarySearch(new_half, target)

        elif data[midpoint] > target:
            other_half = data[:midpoint]

            return recursiveBinarySearch(other_half, target)

    print('nn')


sorted_ = [8, 30, 55,67, 90]
recursiveBinarySearch(sorted_, 67)


