def lengthOfLastWord(s):
    s = s.strip().split(' ')
    return len(s[-1])

print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord("   fly me   to   the moon  "))
print(lengthOfLastWord("luffy is still joyboy"))