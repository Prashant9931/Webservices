class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def add_value(self, value):
        if self.head is None:
            node = Node(value)
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            node = Node(value)
            temp.next = node

    def get_head(self):
        return self.head

    def delete(self, value):
        head_temp = self.head
        # for stating values
        while head_temp.data.emp_id == value:
            temp = head_temp.next
            head_temp = temp

        # any value in the middle
        self.head = head_temp
        temp = self.head
        prev = None

        while temp.next:
            if temp.data.emp_id == value:
                t1 = temp.next
                prev.next = t1
                temp = t1
            else:
                prev = temp
                temp = temp.next
        # for last value
        if temp.data.emp_id == value:
            prev.next = None
