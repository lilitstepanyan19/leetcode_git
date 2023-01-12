def middleNode(head):
        show = head
        fast = head
        while fast and fast.next:
            show = show.next
            fast = fast.next.next
        
        return show

    # x = len(head) // 2
    # ans = []
    # for i in range(x, len(head)):
    #     ans.append(head[i])
    # return ans

print(middleNode([1,2,3,4,5]))
print(middleNode([1,2,3,4,5,6]))