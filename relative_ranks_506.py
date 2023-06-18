def findRelativeRanks(score):
    s = sorted(score, reverse=True)
    ans = []

    for i in score:
        if s.index(i) == 0:
            ans.append("Gold Medal")
        elif s.index(i) == 1:
            ans.append("Silver Medal")       
        elif s.index(i) == 2:
            ans.append("Bronze Medal")
        else:
            ans.append(str(s.index(i) + 1))
        print(s.index(i), i)
    return ans
print(findRelativeRanks([5,4,3,2,1]))
print(findRelativeRanks([10,3,8,9,4]))





    # j = 0
    # k = 4
    # for i in range(len(score)):
        
    #     if score[i] == max(x) :
    #         if j == 0:
    #             c.append("Gold Medal")
    #             x.remove(score[i])
    #             print(score[i])
    #         if j == 1:
    #             c.append("Silver Medal")
    #             x.remove(score[i])
    #             print(score[i])
    #         if j == 2:
    #             c.append("Bronze Medal")
                
    #             print(score[i])
    #         j += 1
    #     else:
    #         c.append(str(k))
    #         # x.remove(score[i])
    #         k += 1