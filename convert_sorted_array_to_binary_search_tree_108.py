class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def sortedArrayToBST(nums):
    def helper(l, r):
        if l <= r:
            mid = (l + r) // 2

            root = TreeNode(nums[mid])
            root.left = helper(l, mid - 1)
            root.right = helper(mid + 1, r)
            return root
    return helper(0, len(nums) - 1)
print(sortedArrayToBST([-10,-3,0,5,9]))