class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        c = 0
        stack = [(root, None)]
        while stack:
            cur, is_left = stack.pop()
            if not cur.left and not cur.right and is_left:
                c += cur.val
            if cur.left:
                stack.append((cur.left, 1))
            if cur.right:
                stack.append((cur.right, 0))
        return c

print(Solution.sumOfLeftLeaves([3,9,20,None, None,15,7]))
print(Solution.sumOfLeftLeaves([1]))