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


ARRAY --> All array operations are index based which makes it faster for all operations except removing an element because deletion requires shifting of all the remaining elements to the front by one position. To push an element to the end of the queue we incremement the end of the queue (end of the array) by one space with the new value.
To dequeue we remove an element from the front of the queue (start of the array). To do this we incremenet from the front of the array(i++), this incremenention automatically discards the element at the start of the queue (not part of queue anymore). (Before we can access and store store this item which we are going to delete from the queue in a variable). 
If we reach maximum array space in memory: we cannot enqueue an element anymore because we cannot incremenet the end of the queue. As we have been dequeue (removing elements from front of queue) it leaves empty space which we can use. This concept is a circular array -- the last item in array is (index = n - 1 --> where n is number of elements in array), to get its next position it's equalled to N % N = 0 (index 0). This means we can incremenent the end of the queue in this interpretation as long as there are empty blocks in memory before the start of array/queue. When the queue is full the next element after the end is the front. (No unused memory cell)
https://www.geeksforgeeks.org/circular-array/
If array gets too full, can either forbit any new elements getting added to queue or create a new bigger space in memory for whole copied array with new elements. The time taken is proportional to number of elements in the array.
Another issue with array implementation comapred to a LL is that the queue may be taking up small space within the allocated memory given to the array = unused memory.


LINKEDLIST --> Easy to enforce FIFO order. Nodes are stored in random places in memory so we can easily change the size of it whenever it is needed. Thus the queue will not overflow and we dont need to worry about working out its capacity. 
Can pick either way (whether head is enqueue or dequeue and vice versa). Depending on how we pick the sides, one will always be 0(1) (case1-enqueue add to head case2-dequeue remove from head) and the other will be 0(n) (case1- remove from tail. case2-enqueue add to tail)
Enqueue (adds node to the back of the queue): create new node, set its next to None as its the last node in the queue change the old tail's reference to refernence our new node. (in DLL) We just have to modify next and prev references so time taken will not depend on number of nodes in DLL. 






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
#         # removes and returns the element at the front of the queue (index 0 first item)
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
        return self.size

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
