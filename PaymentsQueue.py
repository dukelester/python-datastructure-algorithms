#the payment queue
class PaymentQueue:
    #FIFO
    def __init__(self):
        self.payment_queue = []

    def addPayment(self, amount):
        self.payment_queue.append(amount)
        return amount
    
    def removePayment(self, amount):
        if len(self.payment_queue) > 1:
            self.payment_queue.pop(0)
        else:
            print("The queue is empty")
            return self.payment_queue

    def displayPayments(self):
        return self.payment_queue

    def sinzeOfPayments(self):
        return len(self.payment_queue)

employee_payment_queue = PaymentQueue()
print(employee_payment_queue)


employee_payment_queue.addPayment({
    "name":"duke lester",
    "amount": 50000
})
employee_payment_queue.addPayment({
    "name":"Peter lester",
    "amount": 78000
})
employee_payment_queue.addPayment({
    "name":"Janny Monky",
    "amount": 45000
})
my_queue = employee_payment_queue.displayPayments()
print(my_queue)

print(employee_payment_queue.sinzeOfPayments())


'''
The complexity of enqueue
 and dequeue operations in a queue using 
 an array is O(1). If you use pop(N) in python code, 
then the complexity might
 be O(n) depending on the position of the item to be popped.
'''