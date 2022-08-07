from collections import Counter

def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    # return Counter(s1) == Counter(s2)
    return sorted(s1) == sorted(s2)

result = are_anagrams('nameless', 'salesman')
result = are_anagrams('danger', 'garden')
print(result)


def getFirstAndLast(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            start = i
            while i + 1 < len(arr) and arr[i + 1] == target:
                i += 1
            return [start, i]

    return [-1, -1]

result = getFirstAndLast([2,3,4,55,5,5,5,5,5,5,8,4,5,6,6], 5)
print(result)


def kthLargestElement(arr, k):
    for i in range(k-1):
        arr.remove(max(arr))

    return max(arr)

max = kthLargestElement([2,3,4,55,5,5,5,5,5,5,8,4,5,6,6], 4)
print(max)


def sortAndRemove(arr, k):
    n = len(arr)
    arr.sort() #sort the array
    print(arr)
    return arr[n - k]


result = sortAndRemove([2,3,4,55,6,6], 4)
print(result)