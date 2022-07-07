#create a node with data and a pointer

class StudentsNode:
    def __init__(self,marks):
        self.marks = marks  #data
        self.next = None # the pointer

#create the linked list

class StudentMarksList:
    def __init__(self):
        self.head = None #the linked list is empty

if __name__ == '__main__':
    student_list = StudentMarksList()

     # Assign item values
    student_list.head = StudentsNode(1)
    second = StudentsNode(45552)
    third = StudentsNode(3444)
    fourth = StudentsNode(444)

    #connect the nodes 
    student_list.head.next = second
    second.next = third
    third.next = fourth

    # Print the linked list item

    while student_list.head != None:
        print(student_list.head.marks, end=" ")
        student_list.head = student_list.head.next


'''
Linked List Applications
Dynamic memory allocation
Implemented in stack and queue
In undo functionality of softwares
Hash tables, Graphs
'''
