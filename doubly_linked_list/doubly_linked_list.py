# NOTES FROM GUIDED PROJECT


"""Each ListNode holds a reference to its previous node
as well as its next node in the List--> both directions """


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.value)

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to. """

    # Insert a new node after a node somewhere (inbetween 2 nodes)
    # it preserves our code --> order maintained

    def insert_after(self, value):
        # First saves what the current 'next' property is so we can retrieve it to use it for the next property for our new node we want to insert
        # so the current next would be the node to the right of what you are inserting your node into
        # Case: if there is no self.next, below this line, self.next creates a new node and we pass a value to it
        current_next = self.next
        # ListNode: creates (instantiates) a new instance of ListNode class and passes in values we want our new node to have
        # WHY? instead of us defining a new node and linking it to the next and prev one, the class ListNode already gives us the necc. properties to do this, we just have to pass in the values when we call it

        # self.next is now reference to our newly inserted (inbetween 2 nodes) node
        # so current_next refers to the node's next property where our node was inserted in after (so its original pointing position to the node after the one we just inserted before it), so its checking and referncing what that next was pointing to (which was the node after our newly inserted node) and then setting this node's previous property to our newly inserted node (the one to the right of our newly inserted one)
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    # if inserting something at the head, we need to make sure the prev property on the first node (before we add our new one) correctly points to our new node we will add AND make the next value of the newly added node point to the first node (the first node before we add our new one)
    # When we get to creating the new instance of ListNode, because 'self' is passed in, this is already set in the class at the top so it will point to next value so it will add before the current node
    def insert_before(self, value):
        current_prev = self.prev   # 1
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    # Need to make sure prev and next references of the node we want to delete will point to the two nodes before and after this delete node

    def delete(self):
        # Take whatever the previous is pointing to (node to the left of the deleted node), and instead point it to the next node (which is the node to the right of the deleted node)
        # so the self.next on line 57 is currently the deleted node's next which points to the node after it, so now we assign the node on the left side of the node's next value to point at this value
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


# IF HEAD AND TAIL ARE THE SAME NODE --> it tells us that our list that it only has one element in it


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    # Function to print out our linked list values, stops when gets to tail
    # we call this at the bottom
    def print(self):
        curr_node = self.head
        while curr_node.next is not None:
            print(curr_node)
            # moves node onto next (i++)
            curr_node = curr_node.next

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    # This method replaces the head of the list with a new value that is passed in
    # CONSIDER:
    # if no head, or else
    def add_to_head(self, value):
        # Create a new node, dont set any prev or next values at the moment, they already default to none so dont need to pass them in
        new_node = ListNode(value)
        # Incrementing the length to be consistent with values we return
        self.length += 1

        # setting the new node to head and tail (as its one element and FIRST ELEMENT IN THE LIST), if no head or tail means its empty 
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            # now update the head to be our new node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    # removes the head node and returns the value stored in it

    def remove_from_head(self):
        # because we are returning value we need to get this
        value = self.head.value
        # USING OUR DELETE FUNCTION we defined
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    # replaces the tail of the list with a new value that is passed in.

    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1

     # if LL is empty (aka has no head or tail)
        if not self.tail and not self.head:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    # removes the tail node and returns the value stored in it.

    def remove_from_tail(self):
        value = self.tail.value
        # DELETE FUNCTION ALREADY DEFINED
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    # takes a reference to a node in the list and moves it to the front of the list, shifting all other list nodes down.

    def move_to_front(self, node):
        if node is self.head:
            return

        value = node.value

        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            # to shift all the other nodes down 
            self.length -= 1

        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    # takes a reference to a node in the list and moves it to the end of the list, shifting all other list nodes up.

    def move_to_end(self, node):
        if node is self.tail:
            return

        value = node.value

        if node is self.head:
            self.remove_from_head()
            self.add_to_tail(value)
        else:
            node.delete()
            self.length -= 1
            self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail """

    # takes a reference to a node in the list and removes it from the list. The deleted node's previous and next pointers should point to each afterwards
    # we have access to this node by the prev and next pointers as we are passing in the 'node' itself! so we dont need to search through the LL to find the node
    # think about the different types of nodes we can delete so we have different cases

    def delete(self, node):

        # If list is empty we dont want do anything, just return the empty list as there's nothing to delete
        if not self.head and not self.tail:
            return

        # update length
        self.length -= 1

        # If there is only one element aka both head and tail are the same thing (deleting the only node in the list)
        if self.head == self.tail:
            # setting them to none as there's no element to point to
            # as soon as it points to one its LL becomes 0 even though is an element but the node but doesnt point to anything
            # !!!!!!!!!!!! THE LENGTH OF THE LL IS DEFIBED BY THE NUNBER OF NEXT AND PREV NODES IT POINTS TO NOT THE LENGTH OF THE NODES !!!!!!!!!!!!
            self.head = None
            self.tail = None

        # If node is the head node
        elif self.head == node:
            # making the head node equal the old head node (as moving the head pointer to the next element after the head node as we are removing the head node)
            self.head = node.next
            # delete removes the old head node so gets rid of the prev problem of new head
            node.delete()

        # If node is tail
        elif self.tail == node:
            # the node before the tail becomes the new tail node
            self.tail = node.prev
            node.delete()

        #
        else:
            node.delete()

    """Returns the highest value currently in the list"""
    # returns the maximum value in the list.

    def get_max(self):
        if not self.head:
            return None
        max_val = self.head.value
        current_node = self.head
        while current_node:
            if current_node.value > max_val:
                max_val = current_node.value

            # increments so goes through the nodes from head to tail 
            current_node = current_node.next

        return max_val


first_node = ListNode(100)
linked_list = DoublyLinkedList(first_node)
linked_list.add_to_head(1)
linked_list.add_to_head(2)
linked_list.add_to_tail(7)
linked_list.remove_from_head()


linked_list.print()
