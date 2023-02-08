def reverseList(head):
    prev = None
    cur = head

    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev

    # ml = []
    # for el in range(len(head), 0, -1):
    #     ml.append(el)
    # return ml

print(reverseList([1,2,3,4,5]))
print(reverseList([1,2]))
print(reverseList([]))