def maxProfit(prices):
    l, res = 0, 0
    for i in range(1, len(prices)):
        if prices[l] < prices[i]:
            res = max(res, prices[i] - prices[l])    
        else:
            l = i    
    return res

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))
print(maxProfit([7,6,4,3,1]))
# 093324274

# def maxProfit(prices):
#     res = 0
#     for i in range(len(prices) - 1):
#         if prices[i] < prices[i + 1]:
#             res = max(res, max(prices[i:]) - prices[i])        
#     return res