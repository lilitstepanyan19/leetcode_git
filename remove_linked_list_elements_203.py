class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val):
    # demy = ListNode(None, next=head)
    # cur = head
    # prev = demy
    # while cur:
    #     if cur.val == val:
    #         prev.next = cur.next
    #     else:
    #         prev = cur
    #     cur = cur.next
    # return demy.next
    num = []
    for el in head:
        if el != val:
            num.append(el)
    return num
print(removeElements([1,2,6,3,4,5,6], 6))
print(removeElements([], 1))
print(removeElements([7,7,7,7], 7))