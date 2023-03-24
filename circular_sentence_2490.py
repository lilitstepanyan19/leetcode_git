def isCircularSentence(sentence):
    sentence = sentence.split(' ')
    c = 0
    for i in range(len(sentence) - 1):
        if sentence[i][-1] == sentence[i + 1][0]:
            c += 1
    if sentence[-1][-1] == sentence[0][0]:
        c += 1
    if c == len(sentence):
        return True
    return False

print(isCircularSentence("leetcode exercises sound delightful"))
print(isCircularSentence("eetcode"))
print(isCircularSentence("Leetcode is cool"))