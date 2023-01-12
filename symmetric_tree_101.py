def isSymmetric(root):
    def help(r1, r2):
        if not r1 and not r2:
            return True
        if not r1 or not r2:
            return False
        return r1.val == r2.val and help(r1.left, r2.right) and help(r1.right, r2.left)
    return help(root, root)

print(isSymmetric([1,2,2,3,4,4,3]))