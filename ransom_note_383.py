from collections import Counter


def canConstruct(ransomNote, magazine):
    cnt_r = Counter(ransomNote)
    cnt_m = Counter(magazine)
    for k, v in cnt_r.items():
        if cnt_m[k] < v:
            return False
    return True
print(canConstruct("a", "b"))
print(canConstruct("aa", "ab"))
print(canConstruct("aa", "aab"))