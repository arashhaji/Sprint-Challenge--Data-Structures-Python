# from doubly_linked_list import DoublyLinkedList

# class RingBuffer: # a buffer with a dynamic size, so that when it fills up, adding another element must overwrite the first (oldest) one its useful for storing log and history info 
#     def __init__(self, capacity): # sets the capacity to an empty list 
#         self.capacity  = capacity 
#         self.storage = []
        
#     def append(self, item): 
#         self.storage.append(item) # append an element at the end of the list
#         if len(self.storage) == self.capacity:
#             self.cur = 0
#             self.__class__ = self.__Full
    
#     def get(self): # returns a list of items from the oldest to newest 
#             return self.storage
#     class __Full: #checking the length of capacity in the list at its maximum 
#         def __init__(self, n):
#             raise # its a expression 

#         def append(self, x): # add a node for the newest value and removes the newest node 
#             self.storage[self.cur] = x
#             self.cur = (self.cur+1) % self.capacity

#         def get(self): #returns a list of items from the oldest to newest 
#             return self.storage

# # Reference
# # https://www.oreilly.com/library/view/python-cookbook/0596001673/ch05s19.html
# # http://code.activestate.com/recipes/68429-ring-buffer/

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.capacity > self.storage.length:  #checking to see if the list is at capacity 
            self.storage.add_to_tail(item)       # if not we add item to the tail 
            if self.storage.length == 1:         # if the item is already there then replace it with the current value 
                self.current = self.storage.head
        else:
            self.current.value = item            # setting current value to the node 

            if self.current is not self.storage.tail: #if its not the tail we are moving to next one 
                self.current = self.current.next
            else:
                self.current = self.storage.head      

    def get(self):
        content_list = []                      # creating an empty list then looping through the nodes 
        node = self.storage.head               # while loop traversing through the list 
        while node is not None:                # adding value to the list once loop is done 
            content_list.append(node.value)
            node =  node.next                  # moving to the next value 
        return content_list                    # returning the list 

"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""    
    
    def add_to_head(self, value):
        if self.head:
            self.head.insert_before(value)
            self.head = self.head.prev
            self.length += 1
        else:
            self.__init__(node=ListNode(value))

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.head:
            if self.head.next is None:
                self.tail = None
            current_head = self.head.value
            self.head =self.head.next
            self.length -= 1
            return current_head
        else:
            return None

    # def remove_from_head(self):
    #     value = self.head.value
    #     self.delete(self.head)
    #     return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    
    def add_to_tail(self, value):
        if self.tail:
            self.tail.insert_after(value)
            self.tail = self.tail.next
            self.length += 1
        else:
            self.__init__(node=ListNode(value))

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    
    def remove_from_tail(self):
        if self.tail:
            if self.tail.prev is None:
                self.head = None
            current_tail = self.tail.value
            self.tail =self.tail.prev
            self.length -= 1
            return current_tail
        else:
            return None

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        current_node = node
        node.delete()
        self.length -= 1
        self.add_to_head(current_node.value)
    

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        current_node = node
        if current_node.prev is None:
            self.head = current_node.next
        node.delete()
        self.length -= 1
        self.add_to_tail(current_node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node): # store incoming node in variable 
        current_node = node
        if node.prev is None and node.next is None: # this node is the only one on the list 
            self.head = None # removing the value pointing its value to none 
            self.tail = None # removing the value pointing its value to none 
            self.length -= 1 
            return node.value # this value would be deleted/ no longer connected to the list 

        elif node.prev is None: # this checks if the incoming node is deleted from the head 
            self.head = node.next 
            node.delete()
            self.length -= 1 
            return node.value

        elif node.next is None: # this checks if the incoming node is deleted from the tail 
            self.tail = node.prev
            node.delete()
            self.length -=1
            return node.value

        else: 
            node.delete() # removes nodes that are in between the head and tail of the list 
            self.length -= 1
            return node.value
        

        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if not self.head:
            return None

        max_val = self.head.value
        current = self.head
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next
        return max_val