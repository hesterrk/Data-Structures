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

ARRAY --> 



STACK --> Implementing a stack using a linked list is particularly easy because all accesses to a stack are at the top. One end of a linked list, the beginning, is always directly accessible








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
        return self.storage.length

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
