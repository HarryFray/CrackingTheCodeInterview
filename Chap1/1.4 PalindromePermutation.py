'''PalindromePermutation'''
'''works for all cases, counts spaces as char'''
def palindromepermutation(string):
    str = string.lower()
    ascii = [0 for _ in range(128)]
    for char in str:
        if ascii[ord(char)] == 0:
            ascii[ord(char)] = 1
        else:
            ascii[ord(char)] = 0
    if len(str) % 2 == 0 and sum(ascii) == 0:
        return True
    elif len(str) % 2 ==1 and sum(ascii) == 1:
        return True
    else: return False



print palindromepermutation('tacokkcat')