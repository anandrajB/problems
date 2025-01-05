import re
def check_anagrams(s1 ,s2):
    s1_normalized = re.sub(r'[^a-zA-Z]', '', s1).lower()
    s2_normalized = re.sub(r'[^a-zA-Z]', '', s2).lower()
    
    #approach 2 using dict 

    s1_new = ''.join(char for char in s1 if char.isalpha())
    s2_new = ''.join(char for char in s2 if char.isalpha())

    def check_frequency(text):
        found = {}
        for item in text:
            if item in found:
                found[item] += 1
            else:
                found[item] = 1
        return found
    
    return check_frequency(s1_new) == check_frequency(s2_new)

s1 = 'Listen'
s2 = 'Silent'