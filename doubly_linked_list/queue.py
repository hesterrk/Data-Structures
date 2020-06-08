"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
ARRAY -->  To add an value, we add it to the tail and increase the tail by one to point to the next element of the array. If the tail is  the last element of the queue and there are empty blocks before head, the tail will point to the first element of the array and will follow a circular order. If the head of a queue is one more than the tail, the queue is full. To dequeue, we will first store the item which we are going to delete from the queue in a variable because we will be returning it at last. Now, we just have to increase the head pointer by 1. And in the case when the head is at the last element of the array, it will go 1.



LINKEDLIST --> We can change the size of it whenever it is needed. Thus the queue will not overflow and we dont need to worry about working out its capacity. If the queue is empty, we will simply make the new node head and tail of the queue. To dequeue, we need to remove the head of the linked list. 




Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

from doubly_linked_list import DoublyLinkedList
# LIST IMPLEMENTATION

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = list()

#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         # adds value to end of queue
#         self.storage.append(value)
#         self.size += 1

#     def dequeue(self):
#         # removes and returns the element at the front of the queue (index 0)
#         if self.size == 0:
#             return
#         else:
#             self.size -= 1
#             return self.storage.pop(0)


# LINKED LIST implementation

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def __len__(self):
        return self.storage.length

    def enqueue(self, value):
        # adds value to end
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):

        # returns and removes the element from the front of the queue
        if self.size == 0:
            return
        else:
            self.size -= 1
            return self.storage.remove_from_head()
