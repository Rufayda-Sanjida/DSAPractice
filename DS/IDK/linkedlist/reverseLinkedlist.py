class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    current = head
    while current != None:
        tempNext = current.next
        current.next = prev
        prev = current
        current = tempNext


MyNode3 = ListNode(3)
MyNode2 = ListNode(2, MyNode3)
MyNode = ListNode(1, MyNode2)

reverseList(MyNode)
print(MyNode3.next)
#MyNode.next = reference to memory of object
#MyNode.val = actual value


