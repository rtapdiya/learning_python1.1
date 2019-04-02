class Node:
    def __init__(self, value, next = None, prev = None):
        self.data=value
        self.next = next
        self.prev = prev
    def __str__(self):
        return "value is : " + str(self.data) +" next is : " + str(self.next) + " prev is : "+ str(self.prev)

# new_node= Node(2)
# print new_node
# new_node_1 = Node(4,2,1)
# print new_node_1

class DoubleLinkedList:

    def __init__(self):
         self.head= None
         self.tail = None

    def add_first(self,value):
        new_node= Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_last(self,value):
        new_node= Node(value)

        if not self.head:
            self.haed = self.tail = new_node
        else:
            self.tail.next= new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remove_first(self):

        if not self.head:
            raise Exception ( "empty list")
        value = self.head.value
        if self.head == self. tail:
            self.head = self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        return value

    def remove_last(self):
        if not self.head:
            raise Exception("empty list")
        value= self.tail.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            current_node = self.head
            previous_node = None
            while current_node.next != self.tail:
                previous_node = current_node
                current_node = current_node.next
            self.tail.prev = None
            self.tail=current_node
            current_node.next = None
        return value



    def __str__(self):
        current_node=self.head
        accumlated_str=''
        while current_node:
            accumlated_str+=accumlated_str + str(current_node.value)
            current_node=current_node.next
        return accumlated_str