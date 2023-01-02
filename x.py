def lengthOfLongestSubstring(s):
    # def longest_len(x):
    #     for el in x:
    #         if el in s:
    #             return len(el)

    # if s == "":
    #     return 0
    
    # def right(s):
    #     right_min = []
    #     for i in range(len(s)):
    #         y = ''
    #         for j in range(i, len(s)): 
    #             if s[j] not in y:             
    #                 y += s[j]
    #         right_min.append(y)
    #     return right_min

    # def left(s):
    #     left_min = []
    #     for i in range(len(s)):
    #         y = ''
    #         for j in range(len(s)-i): 
    #             if s[j] not in y:             
    #                 y += s[j]
    #         left_min.append(y)
    #     return left_min

    # def center(s):
    #     center_min =[]
    #     for i in range(len(s)):
    #         y = ''
    #         for j in range(i, len(s)-i): 
    #             if s[j] not in y:             
    #                 y += s[j]
    #         center_min.append(y)
    #     return center_min

    # def find_rigth_min(s):
    #     z = ''
    #     for i in range(len(s)):
    #         x = ''
    #         c = s.count(s[i])
    #         if c > 1:
    #             a = s.find(s[i])
    #             z = s[:a]
    #     return z

    # def find_left_min(s):
    #     z = ''
    #     for i in range(len(s)):
    #         x = ''
    #         c = s.count(s[i])
    #         if c > 1:
    #             b = s.rfind(s[i])
    #             z = s[b:]
    #     return z

    # def find_center(s):
    #     z = ''
    #     for i in range(len(s)):
    #         x = ''
    #         c = s.count(s[i])
    #         if c > 1:
    #             a = s.find(s[i])
    #             b = s.rfind(s[i])
    #             z = s[a:b]
    #     return z

    # new_s_right = find_rigth_min(s)
    # new_s_left = find_left_min(s)
    # new_s_center = find_center(s)

    # left_min = left(s)
    # right_min = right(s)
    # center_min = center(s)
    # new_left_min_right = left(new_s_right)
    # new_right_min_right = right(new_s_right)
    # new_center_min_right = center(new_s_right)
    # new_left_min_left = left(new_s_left)
    # new_right_min_left = right(new_s_left)
    # new_center_min_left = center(new_s_left)
    # new_left_min_center = left(new_s_center)
    # new_right_min_center = right(new_s_center)
    # new_center_min_center = center(new_s_center)

    # longest_r = longest_len(right_min)
    # longest_l = longest_len(left_min)
    # longest_c = longest_len(center_min)
    # longest_new_r_right = longest_len(new_right_min_right)
    # longest_new_l_right = longest_len(new_left_min_right)
    # longest_new_c_right = longest_len(new_center_min_right)
    # longest_new_r_left = longest_len(new_right_min_left)
    # longest_new_l_left = longest_len(new_left_min_left)
    # longest_new_c_left = longest_len(new_center_min_left)
    # longest_new_r = longest_len(new_right_min_center)
    # longest_new_l = longest_len(new_left_min_center)
    # longest_new_c = longest_len(new_center_min_center)

    # res = []
    # res.append(longest_r)
    # res.append(longest_l)
    # res.append(longest_c)
    # res.append(longest_new_r)
    # res.append(longest_new_l)
    # res.append(longest_new_c)

    # res.append(longest_new_r_right)
    # res.append(longest_new_l_right)
    # res.append(longest_new_c_right)
    # res.append(longest_new_r_left)
    # res.append(longest_new_l_left)
    # res.append(longest_new_c_left)
    


    # # c_min =[]
    # # r = []
    # # for i in range(len(s)):
    # #     y = ''
    # #     for j in range( len(s)-i):            
    # #             y += s[j]            
    # #     c_min.append(y)
    # # for el in c_min:
    # #     for i in range(len(el)):
    # #         y = ''
    # #         for j in range(i, len(el)):            
    # #                 y += el[j]            
    # #         r.append(y)
    # # cc = r
    # # for el in r:
    # #     r_el = right(el)
    # #     l_el = left(el)
    # #     c_el = center(el)
    # #     f_r_el = find_rigth_min(el)
    # #     f_l_el = find_left_min(el)
    # #     f_c_el = find_center(el)
    # #     # for i in range(len(el)):
    # #     #     if el.count(el[i]) != 1 and el in cc:
    # #     #         cc.remove(el)

    # # longest_r_el = longest_len(r_el)
    # # longest_l_el = longest_len(l_el)
    # # longest_c_el = longest_len(c_el)
    # # longest_f_r_el = longest_len(f_r_el)
    # # longest_f_l_el = longest_len(f_l_el)
    # # longest_f_c_el = longest_len(f_c_el)
    # # res.append(longest_r_el)
    # # res.append(longest_l_el)
    # # res.append(longest_c_el)
    # # # res.append(longest_f_r_el)
    # # # res.append(longest_f_l_el)
    # # # res.append(longest_f_c_el)
    # return max(res)

    start = 0
    max = 0
    d = {}
    if len(s) == 1:
        return 1
    x = ''

    for i in range(len(s)):
        if s[i] in d and d[s[i]] > start:
            start = d[s[i]]
            d[s[i]] = i
            
        else:
            d[s[i]] = i
            if i - start > max:
                max = i - start
    print(d)
    return max

# print(lengthOfLongestSubstring("pwwkew"))
# # print(lengthOfLongestSubstring("abcabcbb"))
# print(lengthOfLongestSubstring("xaxhifdzyuddj"))
# # print(lengthOfLongestSubstring("dvdf"))
# print(lengthOfLongestSubstring("bpoiexpqhmebhhu"))



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




