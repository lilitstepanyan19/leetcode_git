
def addTwoNumbers(l1, l2):
    
    def join_num(num):
        x = []
        for el in num:
            x.append(str(el))
        x.reverse()
        return ''.join(x)

    def split_num(num):
        x = []
        num = str(num)
        num = num[::-1]
        for el in num:
            x.append(el)
        return x

    l1_join = join_num(l1)   
    l2_join = join_num(l2)  

    sum = int(l1_join) + int(l2_join)
    res = split_num(sum)
    return res

print(addTwoNumbers([2,4,3], [5,6,4]))
print(addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9]))

print(addTwoNumbers([0], [0]))
