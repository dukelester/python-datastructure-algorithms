#collection of key:value pairs of data  in {}
#indexed by keys

my_dict = {}
print(my_dict)
my_dict2 = {
    "name":"duke lester", 'age':34, 'location':'juja'
}

print(my_dict2)

my_dict3 = dict([(2,'duke'),(3,'duke'),(4,'duke'),(5,'duke'),(6,'duke')])
print(my_dict3)
my_dict4 = dict(duke=2,age=34,location='juja')
print(my_dict4)

#time complexity to create a dictoionary ==> O(len(dictoionary)) while space complexity O(N)

print(my_dict3[3]) #O(1) for both space and time complexity
my_dict3[3] = 'Lester' #O(1) for both space and time complexity
print(my_dict3[3], my_dict3)

my_dict3["Lester"] = "Software Engineer"
print( my_dict3)

#using update
my_dict3.update({'Programming': "Python Programming"}) #O(1) for both space and time complexity or O(N) for time complexity
my_dict3.update( [(90,"ninty"),('Location', 'Juja')])
print( my_dict3)

#traversing a dict
for key in my_dict3: #O(N) for time complexity O(1) for space complexity
    print(key , '==>:', my_dict3[key])


#search
def search(dict_, value):
    for key in dict_: #O(N) for time complexity O(1) for space complexity
        if dict_[key] == value:
            print(key)
            return f"found at {key}"
        
    return "Not found"

print(search(my_dict3, "Software Engineer"))

#pop() ==> takes in A key and remoces the key and value from a dictoionary

my_dict3.pop(3)
print( my_dict3)
# my_dict3.pop(3)

#popitem() removes the last data in the dictionary +=> Key and value
my_dict3.popitem()
print( my_dict3)

#del() removes a key and a value
del my_dict2['name']
print( my_dict2)
#clear() removes all the elements in a ditionary
my_dict2.clear()
print( my_dict2)

#removing elements is of O(1) for both time and space complexity
print(list(my_dict3.items()))
print(list(my_dict3.values()))
print(list(my_dict3.keys()))

print('duke' in my_dict3)
print('Lester' in my_dict3)

print(all(my_dict3))
print(len(my_dict3))
# print(sorted(my_dict3))

my_dict4 = my_dict3.copy()
print(my_dict4)
print(my_dict4 == my_dict3)
print(id(my_dict4) == id(my_dict3), id(my_dict3), id(my_dict))


fruits_dict = {}

def addFruits(fruit):
    if fruit in fruits_dict:
        fruits_dict[fruit] += 1
    else:
        fruits_dict[fruit] = 1

    print(fruits_dict)

addFruits("Apple")
addFruits("Apple")
addFruits("Orange")
addFruits("Kane")
addFruits("Apple")
addFruits("Apple")
addFruits("Orange")
addFruits("Kane")
addFruits("Apple")
addFruits("Apple")
addFruits("Orange")
addFruits("Kane")


