def detectCapitalUse(word):
    if word.upper() == word or word.lower() == word or word[0].upper() == word[0] \
        and word[1:].lower() == word[1:]:
        return True

    return




print(detectCapitalUse('Aa'))