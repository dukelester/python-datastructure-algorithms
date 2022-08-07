def sortAList(myList):
    sorted_list = []
    
    while myList:
        minimum = myList[0] #arbitrary minimum value
        for number in myList:
            if number > minimum:
                minimum = number
        sorted_list.append(minimum)
        myList.remove(minimum)
    return sorted_list
            
        

results = sortAList([90,434,22,1,3,4,6,88,56])
print(results)
