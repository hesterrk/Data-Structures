"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


from collections import deque
from queue import Queue
from stack import Stack


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# INSERT
    # Insert the given value into the tree
    # compare value to current node, if smaller left, if bigger right
    # if no node to go either left or right make the new node at that spot! --> create a new instance object of the class (BSTNode)
    # dont worry about if no root node

    def insert(self, value):
        # check if new node has bigger or smaller value than our root node (self.value)
        if value < self.value:
            # go left, if there isnt anything on the left side we can place our new node here
            if not self.left:
                # we park our value here as there is not left children for this node (so this node becomes this nodes left child)
                # we call insert() recursively too so it can replicate this down the tree, we pass in the new value
                self.left = BSTNode(value)
            else:
                # Another left node is already here --> we still need to go left and keep looking
                # SO we call insert() again (recursively) on this left node for it to start the process again! and pass the value in so it knows to compare the value like we did above
                self.left.insert(value)

        # Now for right side:
        else:
            if not self.right:
                self.right = BSTNode(value)
            else:
                # we keep looking in that direction
                self.right.insert(value)


# CONTAINS
        # Return True if the tree contains the value
        # False if it does not

        # when we start searching: the self (self.value) will be the root node (only node we have access to)
        # compare the target (value searching for) against the root node (self.value)
        # if target == self.value we can return True
        # if target < self.value go LEFT
        # if target > self.value go RIGHT
        # if target is NOT in our tree -> return false: we know we need to go left or right but theres nothing in those directions. Check if left is a node

        # With this being recursion we need to define our condition for stopping it as it will keep going forever --> return True. We need to termiante the function calls of contains() we have made as we have traversed down the BST as they keep waiting until we get to a concrete return. Now we bubble the answer (target) back up --> the true bubbles back up to its last contains() call which passes the true up to its parent and so forth to the root node where we get our final answer as we first called this function all the way up in the root.

    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            # the self.left is the child left-side node of our root node
            # we now compare this new left node's left and right children with the target
            # now we going to recursively call contains() with same target (not changing what we are looking for) on self.left (calling the function by itself)
            # self.left is a node which because its a node has its own .contains() method on it! --> means this target we have passed in will go and do the same checks again for the target against its own child nodes left and right of this self.left node and itself to see if its equal to it (same goes for self.right node)
            # this is because our self.left node becomes the root node hence the self.value becomes its value

            # left: if there is a left node element doesnt exist
            if not self.left:
                return False
            return self.left.contains(target)

        if target > self.value:  # can just say else here
            # right
            # the self.right is the child right-side node of our root node
            # self.right is also a node which because its a node has its own .contains() method on it!
            if not self.right:
                return False
            return self.right.contains(target)


# MAX
    # Return the maximum value found in the tree aka traverse the node from root to right recursively until right is NULL --> the node whose right is NULL is the node with the maximum value
    # Only one place the max value can exist (right side!)
    # as we loop through the nodes we are selecting the next node from the current node (self) to be the self.right because thats its the child right-side node of our current node, means we keep selecting the right side where the values are increasing as we go down
    # the numbers as you go down on the right side (self.right) increase so we can do a while loop
    # this loop finishes when there is no more self.right of the current node we are on (last one) and the last one would have the max value

    def get_max(self):
        # as we are looping through the while loop we make each of the node going down on right side the current root node (which is reffered to as self)
        # when loop breaks it returns the value (the last node)
        # while there is a right child of the current node present (keep going until no more nodes on right side)
        while self.right:
            self = self.right

        return self.value


# Another implementatation: recursion way
# if not self.right:
    # return self.value

# otherwise: keep going right
# return self.right.get_max()

# Another iterative approach

# current_max = self.value
# current = self
# while current is not None:
#     if current.value > current_max:
#         current_max = current.value

    # update our current max variable if we see a larger value
#     current = current.right

# return current_max


# FOR EACH
    # Call the function `fn` on the value of each node
    # fn is callback that takes value of the node
    # STEPS
    # 1. call forEach on root node --> passes the value of that root node into 'fn'
    # 2. checks self.left and if theres a left: foreach gets called again on that child left node where that node's value gets passed into fn then it checks if that node has left children then for each gets called on that child and so forth until get to a node where there is no self.left child for it
    # 3. none of these functions on the self.left nodes as we went down have finished though as they may have a right children. so we go back up to the previous node and this node has finshed its first if statment (if self.left) now it can get to self.right, if it has right children. so forEach gets called on the right side, then that node on the right side (if there is one), checks its left children if none, checks right, if none go back up to previous node and that can call its right children (if it has some)
    # THIS IS DEPTH FIRST TRAVERSAL: STARTED AT TOP AND WENT DOWN LEFT MOST BRANCH FIRST

    def for_each(self, fn):
        # calling the function on each of the node's value
        fn(self.value)

        # Pass this function to left child
        # recursive call: each node calls the function and passes on both side passes this on to its children until every node in the tree has called the function (fn)
        # when each node calls the function it passes in its value which then gives us access to its children when we say if left or if right and then we get the value of the children etc..
        if self.left:
            self.left.for_each(fn)

        # same for right
        if self.right:
            self.right.for_each(fn)


# Iterative method for this --> aka DFT
    # need a stack to do this operation
    # under the hood recursion uses a stack!

    def iterative_for_each(self, fn):
        stack = []
        # add root node to stack
        stack.append(self)
        # loop while the stack has elements
        while len(stack) > 0:
            # pop off the stack (latest element) in the case of the first time, we have our root node in the stack, so this gets removed
            # second time round the most recent element in our stack which would be the one the root node's left child so this would be removed from stack (most recent element in the stack as we have previously popped off our root node)
            # this popped element now is our new current, so we check if this node has a right or left child, if it does, the right one gets added first then the left one
            current = stack.pop()
            # check node if it has right child, if it does append that child to the stack
            if current.right:
                stack.append(current.right)

            # checks node if it has left child too, if it does it appends it to stack
            if current.left:
                stack.append(current.left)

    # call our function on our current value which is our root node on first time
    # second time round our function is called on our root node's left child node as this is our current node
            fn(current.value)


# ForEach bread first example:
# 1. Start with root node, add it to the queue then remove it
# 2. add right and left child nodes to queue
# 3. call function of root node
# 4. then we remove from the queue our oldest element
# then check for left and right nodes and add them to queue
# and so forth
# remember we have to remove the oldest element (NOT the most recently added element)


   def breadth_first_for_each(self, fn):

    queue = deque()
        # add root node to stack
           queue.append(self)
            # loop while the stack has elements
            while len(queue) > 0:

                # popleft() removes an element from the left side of the deque and returns the value
                # its a method used on the deque!
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)

                fn(current.value)


# Part 2 -----------------------
        # Print all the values in order from low to high
        # Hint:  Use a recursive, depth first traversal --> left to right side

    def in_order_print(self, node):
        # if empty tree
        if node == None:
            return
        if node.left:
            # call the func recursively
            # this in_order_print func takes in a node
            # so it calls this function of the current node (self) and passes in the new left child of it, so then this node gets passed in as the new 'node' in the in_order_Print func's params, so then it asks if this new node has a node.left ...and so forth
            self.in_order_print(node.left)

        print(node.value)

        # get values on left

        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
         # instead of deque, using our queue created from queue file, so we have to use the methods used on this instead
        queue = Queue()

        # start with the given node which is passed in as node (appending this to queue)
        queue.enqueue(node)
        while len(queue) > 0:
            current = queue.dequeue()
            # print current node's value
            print(current.value)

            if current.left:
                queue.enqueue(current.left)

            if current.right:
                queue.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while len(stack) > 0:
            current = stack.pop()
            # print current node's value
            print(current.value)

            if current.right:
                stack.push(current.right)

            if current.left:
                stack.push(current.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
