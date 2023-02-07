def reverseWords(s):

    word = s.split(' ')
    for i in range(len(word)):
        word[i] = word[i][::-1]
    return ' '.join(word)
    
    # ml = []
    # s = s.split(' ')
    # for el in s:
    #     ml.append(el[::-1])
    # return ' '.join(ml)

print(reverseWords("Let's take LeetCode contest"))
print(reverseWords("God Ding"))