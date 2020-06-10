"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

Note: elements can be added and removed from the stack only at the top.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?


ARRAY --> usually pop and push operations are an 0(1) but in a stack they are both 0(n). Append is used as a method to add items to the top of the stack. Because in an array items are stored next to each other in the array's allocated memory block, if the stack grows bigger than this allocated space, then there needs to be more memory given, where the array is copied including the new items appended to the stack to a newer bigger space, which makes some append calls take longer than others. (the size of the array must be specified at time of array decalaration)


STACK --> One end of a linked list, the start, is always directly accessible. There is no memory chunk given to LL as each node can be anywhere in memory. Also unlike arrays, there is never any extra time or memory usage needed for pushing items to the stack. However, the pointers which reference the next and prev nodes to a node (in DLL) require additional memory space (means an additional space of O(n) for every n node linked list). It takes 0(1) to insert or delete node at start. When you add node at the start you need to find current head node and make it the new head node's next property  and assign this new head node as the head. The head of the linked list is the top of the stack



"""


from doubly_linked_list import DoublyLinkedList

# USING A PYTHON LIST


# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = list()

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         # adds an item to the top of the stack
#         self.size += 1
#         self.storage.append(value)

#     def pop(self):
#         # removes and returns the element at the top of the stack (latest/last value)
#         if self.size == 0:
#             return
#         else:
#             self.size -= 1
#             return self.storage.pop(-1)


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        # adds an item to the top of the stack (tail)
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        # returns number that has been popped off stack: the top value (latest)

        if self.size == 0:
            return
        else:
            self.size -= 1
            return self.storage.remove_from_tail()
