def tabulationFib(number):
    series = [0, 1]

    for i in range(2, number + 1):
        series.append(series[i-1] + series[i - 2])

    return series



def numberFactor(number):
    numbers = [1,1,1,2]

    for i in range(4, number + 1):
        numbers.append(numbers[i-1] + numbers[i-3] + numbers[i-4])

    return numbers[number]

print(numberFactor(5))
print(numberFactor(500))


def countChar(my_string):
    result = {}

    for letter in my_string:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    return result


print(countChar("Duke lester"))