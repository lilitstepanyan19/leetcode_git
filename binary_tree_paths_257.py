def binaryTreePaths(root):
    ans = []
    def x(node, path):
        path += str(node.val) + '->'
        if not node.left and not node.right:
            ans.append(path[:-2])
            return
        if node.left:
            x(node.left, path)
        if node.right:
            x(node.right, path)
    x(root, '')
    return ans

print(binaryTreePaths([1,2,3,None,5]))