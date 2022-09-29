'''
!The python ditionaries

These are key-value pairs that are ordered, mutable and indexed by keys. Enclosed in {} and separated by commas
!key : value
The key must be unique
user_info = { 'name':'duke lester', 'age':23, 'location':'Juja'}

one can use the dict() constructor ==> my_data = dict([(name, duke), (age, 12), (location, juja])
'''

my_data = dict([('name', 'duke'), ('age', 12), ('location', 'juja')])
print(my_data)
user_info = { 'name':'duke lester', 'age':23, 'location':'Juja'}
print(user_info)
student_marks = dict([['Monica', 90], ['ken', 69],['mary', 64], ['jane', 80]])
print(student_marks)

student_marks['Monica'] = 70 #! space complexity and time complexity of order 1 ==> O(1)
student_marks['kimberly'] = 39 #! space complexity and time complexity of order 1 ==> O(1)
kimberly_mark = student_marks['kimberly'] #! space complexity and time complexity of order 1 ==> O(1)
print(student_marks,kimberly_mark)

#! using the update(iterable) +++=> adds a key, value pair to the dictionary
student_marks.update({'Morris': 78, 
                      'Kimberly':'Kimberly',  #! space complexity and time complexity of order 1 ==> O(1)
                      'mary':100, 'Monica':50
                      })
print(student_marks)


#! Traverse through a dictionary :: keys(), values() , items()=> methods

for m in student_marks: #! time complexity of order n ==> O(n) and space complexity of O(1)
    mark = student_marks[m]
    print(m ,'==>', mark)
    if mark == 'Kimberly':
        student_marks[m] = 79
print(student_marks)

#! finding a value in a dictionary

def findValue(dictionary, value): 
    for key in dictionary: #! time complexity of order n ==> O(n) and space complexity of O(1)
        if dictionary[key] == value:
            print('**********found ************')
            return f"Found at => {key} "
    return "OOps! Not found"
found = findValue(student_marks, 80)
not_found = findValue(student_marks, 81)
print(found, not_found, sep='\n **')
    

#! Removing an element from a dictionary. ==> Pop(), popitem(), clear()
removed = student_marks.pop('kimberly', 'hello ')
print(removed, 'I was removed recently')
#!  popitem() => removes the last inserted key

last_inserted = student_marks.popitem()
print('I was inserted last ==> ', last_inserted)

#del keyword
del student_marks['mary']
print(student_marks)

#clear()
student_marks.clear()
print(student_marks)
#del
del student_marks
# ! error ==> print(student_marks)

#! DICTIONARY METHODS ==> copy(), get() keys(), values(), items() etc....

#copy()

user_info = {'name':'duke lester', 'age':23, 'location':'Juja'}
user_info['address'] = '45, Juja Street'
print(user_info)

employee_info = user_info.copy()
employee_info['salary'] = 80000
employee_info.update({'company name':'Safaricom', 
                      ' company addres':'Nairobi','Officess':'Kiambu', 
                      'email':'test@company.com', '1':800
                      })
print(employee_info, 'employee info',user_info, sep='\n\n')

#! fromkeys()
sequence = ('emp', 'sal','loc')
emp = employee_info.fromkeys(sequence,)
print(emp)

#! get() ==> gets an element based on the key
my_salary = employee_info.get('salary', None)
print('my salary is ==> ', my_salary)
trips = employee_info.get('company trips', "No trips!")
print('The company offers ', trips)

#! items() ==> turns the dictionary into a list of tuples made of each key and value ==> (key, value)
emp_items = employee_info.items()
print(emp_items)

#! Keys() ==> list of keys in the dictionary
my_keys = employee_info.keys()
print(list(my_keys))

#! Values() ==> list of values in the dictionary
my_values = employee_info.values()
print(list(my_values))

#! setdefault()
employee_info.setdefault('company email', 'lester@delester.com')
print(employee_info)

if 'company email' in employee_info:
    print('Yees ! found inside')
else:
    print('not inside')
    

#!all()
if all(str(employee_info.keys()) ):
    print('yeeeey Trueeeee')
else:
    print('NAAAAAAAH')
    
    #!any()
if any(employee_info.keys()):
    print('Yees ! found employee_info')
else:
    print('Not found in any')
    
#!len()
print(len(employee_info))
sorted_employee_info = sorted(employee_info, reverse=True)
print(sorted_employee_info)


fruits_dict = {}
def addOneFruit(fruit):
    if fruit in fruits_dict:
        fruits_dict[fruit] += 1
    else:
        fruits_dict[fruit] = 1
    print(fruits_dict)
    
addOneFruit('Mango')
addOneFruit('Mango')
addOneFruit('Pinneaple')
addOneFruit('oranges')
addOneFruit('bananas')
addOneFruit('Mango')
addOneFruit('Mango')
addOneFruit('Pinneaple')
addOneFruit('oranges')
addOneFruit('bananas')
        
