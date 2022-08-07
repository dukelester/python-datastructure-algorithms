import os
def myFunction():
    pass

#lambda function  ==> anonymous

myArea = lambda radius : radius **2 * 3.124
print(myArea(56))


print(bin(int(myArea(50))))

name = "duke lester"

in_bytes = bytes(name, 'utf-8')
print(in_bytes)

print(callable(myArea))

# compile string source to code  
code_str = 'x=5\ny=10\nprint("sum =",x+y)'  
# code = compile(code_str, 'sum.py', 'exec')  
# exec(code)  
# exec(x)  

print(sum([7,9,2,380]))


myNumbers = [7,9,2,380]
if any(myNumbers) > 10:
    print(sum([7,9,2,380]))
else:
    print('not found')

letters = ('m', 'r', 'o', 't', 's')  
  
fSet = frozenset(letters)  
print('Frozen set is:', fSet)  
print('Empty frozen set is:', frozenset())  

mapped = map(lambda data: data * 2, myNumbers)
# print(set(mapped))
print(list(memoryview(bytearray('letters', 'utf-8'))), 'here')
comp = complex(20,8)
comp_ = complex(56, 89)
print(comp + comp_)

files = dir()
print((files))

print(divmod(4, 3))
print(divmod(45, 9))

nums = [7,9,2,380]
numbers_enum = enumerate(nums)
print(list(numbers_enum))

#filter

filtered = filter(lambda x : x % 2 == 0, nums)
print(list(filtered))

name = "duke lester"
print(hash(name))

small = min(2225,325,2025) # returns smallest element  
small2 = min(1000.25,2025.35,5625.36,10052.50)  

print(small, small2)

minimum = min(nums)
print((minimum))

set_ = set(name)
print(set_)

numList = [4,5, 6, 9, 567, 54]  
strList = ['four', 'five', 'six']  

zipped = zip(numList, strList)
print(list(zipped))


squared = list(map(lambda x: x**2, nums))
print(squared)

squares = [lambda num1 = num1: num1 ** 2 for num1 in range(0, 11)]  
print(squares)

with open("./CheckForElementInarray.py", 'r+') as myFile:
    contents = myFile.read()
    print(contents)
    myFile.close()


with open("./PrimeNumbers.py", "r") as file2:
    contents = file2.readline()

    print("\n" + contents)
    contents_ = file2.read()

    from_file = []
    for cont in contents_:
        
        from_file.append(cont)
    print(from_file)

    file2.close()


with open("./merge.txt", "w") as merge:
    # content = merge.read()
    # print(content)
    merge.write('''Python is the modern day language. It makes things so simple.\n 
                    It is the fastest-growing programing language''')  
    merge.close()


# newFile = open("./myfile.txt", 'x')
with open('./myfile.txt', 'a+') as myFile:
    myFile.write("Hello this is duke lester and a file reading")

    print(myFile.tell())

#rename a file
os.rename("./merge.txt", "./merge2.txt")

os.remove("./myfile.txt")

#create a directory
# os.mkdir("./folder2")
os.chdir("./folder2/")
# open("./myfile.txt", "x")

print(os.getcwd())

# os.rmdir("./folder2")
