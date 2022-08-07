def findGCD(num1, num2):
    if num1 or num2 < 0:
        return 1
    if num1 ==0 and  num2 == 0:
        return -1

    if int(num1) != num1 or int(num2) != num2:
        return "Please enter integers only"

    elif num1 < 0:
        num1 = -num1

    elif num2 < 0:
        num2 = -num2

    elif num2 == 0: #base condition
        return num1

    else:
        return findGCD(num2, num1 % num2)


print(findGCD(60, 36))
