class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
    
print(Solution.deleteNode([4,5,1,9],5))