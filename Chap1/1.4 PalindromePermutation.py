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


# -----------------------------------------------------------------------------------------------
'''solution'''

def pal_perm(phrase):
    '''function checks if a string is a permutation of a palindrome or not'''
    table = [0 for _ in range(ord('z') - ord('a') + 1)]
    countodd = 0
    for c in phrase:
        x = char_number(c)
        if x != -1:
            table[x] += 1
            if table[x] % 2:
                countodd += 1
            else:
                countodd -= 1

    return countodd <= 1

''' removing all non letters from string accounting for upper and lower'''
def char_number(c):
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    val = ord(c)

    if a <= val <= z:
        return val - a
    elif A <= val <= Z:
        return val - A
    return -1

#print palindromepermutation('tacokkcat')
print pal_perm('taco cat')
