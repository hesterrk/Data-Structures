
from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.size = 0
        self.limit = limit
        self.structure = DoublyLinkedList()
        # dict stores key value pairs
        self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    # Getting item
    # 1. looks up item by key, gets entry and moves that item to head
    # note the self.storage[key] is just a node in our DLL
    def get(self, key):
        if key in self.storage:
            # move entry to front by the method move_to_front in DLL (picks up an element we select and makes it head) this method passes in the node (element we want to move!) so we access the value of element by passing in key in a dict-acess style
            self.structure.move_to_front(self.storage[key])
            # return the value of head now
            return self.storage[key]

        else:
            # returns none as no entry
            return None

    """
   1. Adds the given key-value pair to the cache.
    2. The newly-added pair should be considered the most-recently used entry in the cache (head)
    3. If the cache is already at max capacity before this entry is added, then the oldest entry in the cache needs to be removed to make room. 
    4. If the key already exists in the cache, we simply want to overwrite the old value associated with the key with the newly-specified value.
    """

    # make new element the head of DLL
    # add key to hash table
    # check if its over limit, if so delete the oldest entry
    # if key exists overwrite it with new key and value

    # def set(self, key, value):
    #     # 4. First check if key exists and if so overwrite it with new key and value + move it to front
    #     if key in self.storage:
    #         # getting value by its key
    #         new_entry = self.storage[key]
    #         # overwriting value of the key
    #         new_entry = value
    #         # moving existing key to head (as its latest)
    #         self.structure.move_to_front(self.storage[key])

    #     # Check if enough space if so add new key by increasing length  DLL size, if not remove last item (tail)
    #     if self.size is self.limit:
    #         # not enough space --> get rid of tail, find tail an delete it (remove_from _tail())
    #         remove = self.structure.remove_from_tail()
    #         del self.storage[remove]

    #         self.size -= 1
    #         # we make the new value the head. The method add_to_head doesnt need to know the value, just knows theres a key
    #     self.structure.add_to_head(key)
    #     # Making our new entry the head in DLL
    #     self.storage[key] = self.structure.head
    #     # Our DLL increases by one
    #     self.size += 1



    # !! important !!
    # Stored the tupe or dict in the node in DLL
    # In our dict we store the reference (key) to the node with the key:value pair in it, so access the tuple value which is stored in the node: we have to go into dict using the key and find the node and through the node read the second value of the tuple to get the value
    # SO when we delete the tail in our DLL, we use the tail's value (contains key: value pair) to access the key gives us the name of the key which we pass into the dict. as the dict requires a key to know what key to delete in the dict itself (removes the key pointing to the node in the DLL which contains the key:value pair)

    def set(self, key, value):

        # IF key is in storage have to set the key to this new value coming in from params and have to MOVE this entry to the front of the DLL as most recently used
        # --> to do this we have to find the key, remove it and move it to front (move_to_front())
        if key in self.storage:
            node = self.storage[key]
            # whatever is stored in this node above, we need to update the node's value
            # node.value is whatever is held inside the node = which is the key:value pair in the dict --> { key: "hi", value: "value"}
            node.value = (key, value)
            self.structure.move_to_front(node)
            return

        # If the limit has been hit:
          # remove oldest node (tail)
        # delete that key:value node in our dict
        if self.size == self.limit:
            # need to delete the reference to the key that points to this node's value in our dict (deletes the key:value)
            # we pass our DLL position of the tail into dict to get the index of where the tail is stored in the dict, we then need to access value of the tail in order for it to be deleted. The value of the tail is a tuple (node.value) so we need to access the key part so thats index 0 (first item of the value of the tail node)
            del self.storage[self.structure.tail.value[0]]
            # remove from tail node from DLL
            self.structure.remove_from_tail()
            # update the size
            self.size -= 1


        # Add the new node to storage
        # the value we are adding to the head: the Tuple of key:value --> now the node value is storing the key and value
        # now the head has this node 
        self.structure.add_to_head((key, value))

        # The self.storage[key]: the key is a string and it has a new value assigned to it (self.structure.head) which is a node! so now there is a key referncing our newly added node
        # this key is a string. Referencing the node from the string key 
        self.storage[key] = self.structure.head
        #updating the size
        self.size +=1







    
