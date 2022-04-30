class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    #traverse through linked list
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insertAfter(self,prev_node,new_data):
        new_node=Node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node

    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node








if __name__=='__main__':
    llist=LinkedList()
    llist.head=Node(1)
    second=Node(2)
    third=Node(3)
    llist.head.next = second
    second.next = third

    llist.push(20)
    llist.append(11)
    llist.append(99)
    #llist.printList()

    llist.delete_node(11)
    llist.printList()



