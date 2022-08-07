#remove duplicates  from a linked list
def remove_duplicates(linkedList):
    visited = []

    if linkedList.head is None:
        return "Empty list"

    else:
        current_node = linkedList.head
        while current_node.next:
            if current_node.next.data in visited:
                current_node.next = current_node.next.next
                continue
            else:
                visited.append(current_node.next.data)
                current_node = current_node.next
        return visited


#or
def removeDuplicates(linkedList):
       if linkedList.head is None:
            return None
       else: 
            current_node = linkedList.head
            visited = set([current_node.value])
            while current_node.next:
                  if current_node.next.value in visited:
                        current_node.next = current_node.next.next
                  else:
                        visited.add(current_node.next.value)
                        current_node = current_node.next
            return linkedList 


# Implement a code to find the Kth to last element in a singly linked list.

def findKthToLast(linkedList, k):
    #declare 2 pointers
    first_pointer = linkedList.head
    second_pointer = linkedList.head

    for i in range(k):
        if second_pointer is None:
            return None

        second_pointer = second_pointer.next

    while second_pointer:
        first_pointer = first_pointer.next
        second_pointer = second_pointer.next

    return first_pointer


#Code to partition the linked list around a value 'x'
def partition(linkedList, x):
       current_node = linkedList.head
       linkedList.tail = linkedList.head   
            
       while current_node: 
               next_node = current_node.next
               current_node.next = None
               if current_node.value < x:
                    current_node.next = linkedList.head
                    linkedList.head = current_node
               else:
                    linkedList.tail.next = current_node
                    linkedList.tail = current_node
               current_node = current_node.next    
       if linkedList.tail.next is not None:
               linkedList.tail.next = None  


#Code to return the sum of two numbers represented by linked lists
def sumList(linkedList1, linkedList2):
       num1 = linkedList1.head
       num2 = linkedList2.head   
       carry = 0
       newLL = SinglyLinkedList()
            
       while num1 or num2: 
               result = carry
               if num1:
                    result += num1.value
                    num1 = num1.next
               if num2:
                    result += num2.value
                    num2 = num2.next
               newLL.add(int(result % 10))  
               carry = result /10
       return newLL  


            

#Code to check whether two lists are intersecting
def intersection(linkedList1, linkedList2):
       if linkedList1.tail is not linkedList2.tail:
             return False       
       lenA = len(linkedList1)     
       lenB = len(linkedList2) 
       shorter = linkedList1 if lenA < lenB else linkedList2
       longer = linkedList2 if lenA < lenB else linkedList1
       diff = len(longer) - len(shorter)
       longer_node = longer.head
       shorter_node = shorter.head

       for i in range(diff):
            longer_node = longer_node.next
       while shorter_node is not longer_node:
            shorter_node = shorter_node.next
            longer_node = longer_node.next 
       return longer_node