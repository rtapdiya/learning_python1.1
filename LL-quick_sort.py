from main.linked_list import LinkedList

def quick_sort_linked_list(self):
    quick_sort_helper ( self, self.head, self.tail)


def quick_sort_helper(self, start , end):
    if start == end :
        return

    start, end, new_start, new_end = partition(self, start, end)
    quick_sort_helper(self, start, end)
    quick_sort_helper(self, new_start, new_end)


def partition(self, start, end):

    prev = None
    current = start
    new_tail = end

    while current != end:
        if  current.data >= end. data:
            if prev:
                prev.next = current.next
            temp = current.next
            new_tail.next = current
            current.next = None
            current = temp
        else:
            prev = current
            current = current.next
    return (start, prev, end.next, new_tail)
