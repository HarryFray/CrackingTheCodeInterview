def Permutation(string1,string2):
    if string1.find(string2) != -1 or string2.find(string1) != -1:
        return True
    return False

print Permutation('nick ', 'nick is great')



