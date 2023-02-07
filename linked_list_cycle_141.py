def hasCycle(head):
    seen = set()
    while head:
        if head in seen:
            return True
        seen.add(head)
        head = head.next
    return False


print(hasCycle([3,2,0,-4]))
print(hasCycle([1,2]))