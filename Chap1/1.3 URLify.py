''''''
''' my code does not account for extra spaces or given length'''
def URLify(string):
    newstring = ''
    for char in string:
        if char == " ":
            newstring += '%20'
        else: newstring += char
    return newstring

#########################################################


def urlify(string, length):
    '''function replaces single spaces with %20 and removes trailing spaces'''
    new_index = len(string)

    for i in reversed(range(length)):
        if string[i] == ' ':
            # Replace spaces
            string[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            # Move characters
            string[new_index - 1] = string[i]
            new_index -= 1

    return string

print urlify('MR Nick Fray',10)


