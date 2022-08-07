import collections

dequeue = collections.deque(['23', '23',])
dequeue.insert(2, 233)
dequeue.insert(0, 78)
print(dequeue)