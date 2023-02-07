from collections import deque

# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def minDepth(root):
    if not root:
        return 0
    q = deque([(root, 1)])
    while q:
        cur, dept = q.popleft()
        if not cur.left and not cur.right:
            return dept
        if cur.left:
            q.append((cur.left, dept + 1))
        if cur.right:
            q.append((cur.right, dept + 1))
    return

print(minDepth([3,9,20,None, None,15,7]))