# create a node

class EmployeesNode:
    def __init__(self,employee_data):
        self.employee_data = employee_data
        self.next = None

#create a linked list
class EmployeeLinkedList:
    def __init__(self):
        self.head = None
