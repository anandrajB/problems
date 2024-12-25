def repeatedSubstringPattern(str):
    return str in (2 * str)[1:-1]


repeatedSubstringPattern("abab")
