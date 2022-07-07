# create a node

class EmployeesNode:
    def __init__(self,employee_data):
        self.employee_data = employee_data
        self.next = None

#create a linked list
class EmployeeLinkedList:
    def __init__(self):
        self.head = None

    #insert the employee at the beginning of the Employee linked list
    def insertEmployeeAtBeginning(self, emp_data):     
        new_employee = EmployeesNode(emp_data) #allocating memory to the node.
        new_employee.next = self.head
        self.head = new_employee
        print(f" Inserted {new_employee} at the beginning of the Linked list")
        return new_employee
    #insert an employee at the end of  the linked list
    def insertEmployeeAtEnd(self, emp_data):
        new_employee = EmployeesNode(emp_data) #allocating the memory
        if self.head == None:
            self.head = new_employee
            return f'Since the linked list is empty then the {new_employee}  is first'
        last_employee = self.head
        while (last_employee.next):
            last_employee = last_employee.next
        last_employee.next = new_employee

    #insert at a particular position in the linked list
    def insertEmployeeAtPosition(self, previous_employee, new_employee):
        if previous_employee is None:
            print("the node must be inside the employee list")
            return f'we cannot insert'
        new_employee = EmployeesNode(new_employee) #allocating  memory
        new_employee.next = previous_employee.next
        previous_employee.next = new_employee

        return f'Insert complete'
    #deleting an employee
    def deleteEmployee(self, employee):
        if self.head is None:
            return f'we cannot delete since the linked list is empty'
        temporary_employee = self.head

        if employee == 0:
            self.head = temporary_employee.next
            temporary_employee = None
            return f'Deleted the first employee in the linked list'
        #find the employee to be deleted
        for emp in range(employee - 1):
            temporary_employee = temporary_employee.next
            if temporary_employee is None:
                break
        #if the employee is not present in the linked list
        if temporary_employee is None:
            return f'No empoloyee found under the record'

        if temporary_employee.next is None:
            return f'None'
        next = temporary_employee.next.next
        temporary_employee.next = next

    #search for an employee
    def searchEmployee(self, employee):
        current_employee = self.head

        while current_employee is not None:
            if current_employee.employee_data == employee:
                return True
            current_employee = current_employee.next
        return False

    #sort the employees

    def sortEmployees(self, head):
        current = head
        index = EmployeesNode(None)

        if head is None:
            return f'The head is None'
        else:
            while current is not None:
                #index points to the node next to the current
                index = current.next

                while index is not None:
                    if current.employee_data > index.employee_data:
                        current.employee_data, index.employee_data = index.employee_data, current.employee_data
                    index = index.next
                current = current.next


    #display the data about the employees
    def printingTheList(self):
        temp = self.head
        while temp:
            print(str(temp.employee_data) + " " )
            temp = temp.next

if __name__ == '__main__':
    myList = EmployeeLinkedList()
    myList.insertEmployeeAtBeginning({
        "name": "duke Lester",
        "age": 23,
        "salary":67000, 
        "company": "Google"
    })
    myList.insertEmployeeAtBeginning({
        "name": "Toby Markie",
        "age": 45,
        "salary":97000, 
        "company": "Facebook"
    })
    myList.insertEmployeeAtBeginning({
        "name": "Monica Gazzy",
        "age": 34,
        "salary":45000, 
        "company": "Twitter"
    })

    myList.insertEmployeeAtEnd({
         "name": "Jeremy Smith",
        "age": 36,
        "salary":56000, 
        "company": "Twitter"
    })
    myList.insertEmployeeAtEnd({
         "name": "Henry Facmine",
        "age": 36,
        "salary":56000, 
        "company": "Twitter"
    })

    myList.insertEmployeeAtPosition(myList.head.next, {
        "name": "Mercy Kimoni",
        "age": 34,
        "salary":78000, 
        "company": "TikTok"
    })
    myList.printingTheList()
    myList.deleteEmployee(0)
    myList.printingTheList()
        
    # myList.sortEmployees(myList.head)
    # print('sorted list')
    # myList.printingTheList()









