
''''''
'''string are imutable 
   do not use any other data structures'''
'''
def IsUnique(string):
    for char in string:
       if char in string[string.find(char)+1:]:
           return 'not unique'
    return 'unique'

print IsUnique('qmkfirt  ')
'''
def unique(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        # assigns True to found char in char_set
        char_set[val] = True

    return True

print unique('abcse%$^$')