''''''
'''code runs correctly however there is plenty of room for impovment
strcount is not req before the 4 loop. should use range in loop not char'''
def StringCompression(str1):
    count = 1
    newstr = ''
    strcount = 1
    for char in str1:
        ''' prevents from going outside of string size'''
        if strcount < len(str1):
            '''finds next charicter '''
            nextchar = str1[strcount]
            strcount += 1
            '''adds 1 to count if duplicate is found'''
            if char == nextchar:
                count +=1
                ''' prints new string with number of char found'''
            else:
                newstr += (char + str(count))

                count = 1
        else:
            ''' adds final count and letter should be able to do this above somehow'''
            return newstr + str1[-1:] + str(count)
print StringCompression('aabbbbddss')