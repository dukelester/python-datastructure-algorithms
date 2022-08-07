def decimalToBinary(number):
    if number == 0:
        return 0
    elif number < 0 or int(number) != number:
        return "please use integers only"

    else:
        # return (number % 2) + 10 * decimalToBinary(int(number / 2))
        return (number % 2) + 10 * decimalToBinary(int(number/2))

print(decimalToBinary(7))
print(decimalToBinary(100))
print(decimalToBinary(-100))


def fac(n): 
  if n==0: 
    return 1 
  else: 
    return n*fac(n-1) 
print(fac(3))

def countTime(time):
    if time == 0:
        return 
    else:
        print(time)
        countTime(time -1 )

countTime(70)

def findFactorial(n):
    if n == 1:
        return 1

    else:
        return n * findFactorial(n-1)

print(findFactorial(9))


def reverseList(list_, k, m):
    if k < m:
        current = list_[k]
        list_[k] = list_[m]
        list_[m] = current

        reverseList(list_, k+1, m-1)
        print(current)

reverseList([8,2,4,6,78,9], 0, 5)


def reverseString(my_string):
    if len(my_string) == 0:
        return my_string

    else:
        return reverseString(my_string[1:] ) + my_string[0]

print(reverseString("duke lester"))


def maximum(arr):
    if len(arr) ==0:
        return arr[0]

    else:
        m = max(arr[1:])
        return m if m > arr[0] else arr[0]

print(maximum([9,3,4,6,2,512,44,56]))