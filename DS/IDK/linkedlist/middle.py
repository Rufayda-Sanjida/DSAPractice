class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middle(head):

    myList = []
    current = head 
    while current != None:
        myList.append(current.val)
        holder = current.next
        current = holder
    
    middle = len(myList) // 2
    print(myList[middle])


MyNode4 = ListNode(4)
MyNode3 = ListNode(3, MyNode4)
MyNode2 = ListNode(2, MyNode3)
MyNode = ListNode(1, MyNode2)

middleNode = middle(MyNode)
print(middleNode)
#MyNode.next = reference to memory of object
#MyNode.val = actual value


