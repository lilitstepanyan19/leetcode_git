# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def postorderTraversal(root):
    ans = []
    def x(node):
        if node:
            x(node.left)
            x(node.right)
            ans.append(node.val)
    x(root)
    return ans

print(postorderTraversal([1,'null',2,3]))
print(postorderTraversal([]))
print(postorderTraversal([1]))