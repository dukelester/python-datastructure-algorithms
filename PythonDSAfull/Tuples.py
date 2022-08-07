#immutable sequancial data structure
tem= ("cat", [6,3,2,3])
trm = 8,3,4,5,6  #tuple packing

#O(1) time complexity and O(N) for space complexity  on creating a tuple


def search(tuple_, element):
    for k in tuple_:
        if k == element: #time ==> O(N) space complexity O(1)
            print(tuple_.index(k))
            return tuple_.index(k)

        else:
            print('Not found')
search(tem, "cat")

result = tem + trm
print(result)
print(result * 3)
print(3 in result)
print((result*3).count(3))
print(len(result *3))  #length of the tuple
print(max(result[1]*3))
print(min(result[1]))

my_tuple = tuple([7,3,4,2,24])
print(my_tuple)
print(result[::-1])

name = "duke lester"
data = tuple([ i for i in name])
print(data)

