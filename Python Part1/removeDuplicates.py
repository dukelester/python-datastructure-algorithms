list1 = [1,2,2,3,55,98,65,65,13,29]  

list2 = []

for element in list1:
    if element not in list2:
        list2.append(element)

print(list2)

list1 = [1,2,3,4,5,6]  
list2 = [7,8,9,2,10]  

for element in list1:
    for element_ in list2:
        if element == element_:
            print(element_)

# print(cmp(list1, list2))

Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}    
# print(Days)

for day in Days:
    print(day)

months = set(["January","February", "March", "April", "May", "June"])    
months.add("December")
print(months)
months.update(["July","August","September","October","November","December"])
print(months)
months.discard("January");    
print(months)
months.remove("December")
print(months)

employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}    
for emp in employee.values():
    print(emp)

#loop through the items
for item in employee.items():
    print(item)

print(employee.get("Age"))

