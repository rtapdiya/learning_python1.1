class Node:
    def __init__(self, value, next = None, prev = None):
        self.value=value
        self.next = next
        self.prev = prev
    def __str__(self):
        return str(self.value)
        # return "value is : " + str(self.data) +" next is : " + str(self.next) + " prev is : "+ str(self.prev)


# new_node= Node(2)
# print new_node
# new_node_1 = Node(4,2,1)
# print new_node_1


class DoubleLinkedList:

    def __init__(self):
         self.head= None
         self.tail = None
         self.size=0

    def add_first(self,value):
        new_node = Node(value)
        self.size+=1
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_last(self,value):
        new_node= Node(value)
        self.size+=1
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
            self.size-=1
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
            self.size-=1
        return value

    def remove_last(self):
        if not self.head:
            raise Exception("empty list")
        value= self.tail.value
        if self.head == self.tail:
            self.head = self.tail = None
            self.size-=1
        else:
            current_node = self.head
            previous_node = None
            while current_node.next != self.tail:
                previous_node = current_node
                current_node = current_node.next
            self.tail.prev = None
            self.tail=current_node
            current_node.next = None
            self.size-=1
        return value

    def remove_at_nth_position(self,position):

        if position < 0 or position > self.size:
            raise Exception( " Invalid Position")
        if position == 0:
            self.remove_first()
        if position == self.size-1:
            self.remove_last()
        if position >= 1 and position < self.size:
            previous_value= None
            current_value = self.head
            count=0
            while count <> position:
                previous_value = current_value
                current_value = current_value.next
                count+=1
            value = current_value
            previous_value.next = current_value.next
            current_value.next.prev = previous_value
            current_value.prev = current_value.next = None
            self.size-=1
            return value


    def __str__(self):
        current_node=self.head
        accumlated_str=''
        while current_node:
            accumlated_str += str(current_node.value)
            current_node=current_node.next
        return accumlated_str