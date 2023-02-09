class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(root1, root2):
    if not root1 and not root2:
        return None
    if not root2:
        return root1
    if not root1:
        return root2
    
    new_root = TreeNode(root1.val + root2.val)
    new_root.left = mergeTrees(root1.left, root2.left)
    new_root.right = mergeTrees(root1.right, root2.right)
    return new_root

print(mergeTrees([1,3,2,5], [2,1,3,None,4,None,7]))